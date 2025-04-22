import os
import subprocess
import itertools

class CommandRunner:
    def __init__(self, base_dir: str, python_path: str):
        self.base_dir = base_dir
        self.python_path = python_path
        self.tests_dir = os.path.join(self.base_dir, 'tests')
        self.results_dir = os.path.join(self.base_dir, 'results')
        self.create_results_dir()
        self.test_files = self.get_test_files()
        self.test_suites = self.generate_test_suites()
        self.run_tests()

    def create_results_dir(self) -> None:
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
            print(f'Created directory: {self.results_dir}')
            print('Results will be stored here.')
        else:
            print(f'Directory {self.results_dir} already exists.')
            print('Results will be appended to existing files.')
            print('To clear the results, delete the directory and run the script again.')
            print('NOTE: This script will not overwrite existing files.')
    
    def get_test_files(self) -> list:
        test_files = []
        for root, _, files in os.walk(self.tests_dir):
            for file in files:
                if file.endswith('.py') and 'test' in file:
                    test_files.append(os.path.join(root, file))
        return test_files
    
    def generate_test_suites(self) -> list:
        test_suites = []
        for test_file in self.test_files:
            test_suite_name = os.path.splitext(os.path.basename(test_file))[0]
            test_suite = f'python -m unittest {test_file}'
            test_suites.append((test_suite_name, test_suite))
        return test_suites
    
    def run_tests(self) -> None:
        print('Running tests...')
        for test_suite_name, test_suite in self.test_suites:
            print(f'Running test suite: {test_suite_name}')
            result_file = os.path.join(self.results_dir, f'{test_suite_name}.txt')
            with open(result_file, 'a') as result_file:
                result_file.write(f'Test suite: {test_suite_name}\n')
                result_file.write(f'Python path: {self.python_path}\n')
                result_file.write(f'Test files: {", ".join(self.test_files)}\n\n')
                result_file.write('Test results:\n')
                process = subprocess.Popen(test_suite, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                result_file.write(stdout.decode('utf-8'))
                if stderr:
                    result_file.write(f'\nError: {stderr.decode("utf-8")}\n')
                    print(f'Error: {stderr.decode("utf-8")}')
                else:
                    print('Test suite completed successfully.')
                    print(f'Results saved to: {result_file.name}')
                    print('---')
    
    def run_parallel_tests(self, num_processes: int) -> None:
        print('Running tests in parallel...')
        if num_processes <= 0:
            print('Number of processes must be greater than 0.')
            return
        
        test_suites_per_process = len(self.test_suites) // num_processes
        leftover_tests = len(self.test_suites) % num_processes
        
        processes = []
        for i in range(num_processes):
            start_index = i * test_suites_per_process
            end_index = start_index + test_suites_per_process
            if i < leftover_tests:
                end_index += 1
            test_suites_subset = self.test_suites[start_index:end_index]
            test_suite_names = [suite_name for suite_name, _ in test_suites_subset]
            test_suite_commands = [f'python -m unittest {test_suite}' for _, test_suite in test_suites_subset]
            process = subprocess.Popen(test_suite_commands, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            processes.append((test_suite_names, process))
            print(f'Running test suite subset: {", ".join(test_suite_names)}')
            print(f'Test suite commands: {", ".join(test_suite_commands)}')
            print(f'Process ID: {process.pid}')
            print('---')
    
        for test_suite_names, process in processes:
            stdout, stderr = process.communicate()
            result_file = os.path.join(self.results_dir, f'{"".join(test_suite_names)}.txt')
            with open(result_file, 'a') as result_file:
                result_file.write(f'Test suite: {"".join(test_suite_names)}\n')
                result_file.write(f'Python path: {self.python_path}\n')
                result_file.write(f'Test files: {", ".join(self.test_files)}\n\n')
                result_file.write('Test results:\n')
                if stderr:
                    result_file.write(f'\nError: {stderr.decode("utf-8")}\n')
                    print(f'Error: {stderr.decode("utf-8")}')
                else:
                    print('Test suite subset completed successfully.')
                    print('All tests completed.')
    
    def generate_report_xml(self) -> None:
        report_xml_file = os.path.join(self.results_dir,'report.xml')
        test_suites_xml = '<testsuites>'
        for test_suite_name, test_suite in self.test_suites:
            result_file = os.path.join(self.results_dir, f'{test_suite_name}.txt')
            with open(result_file, 'r') as result_file:
                test_suite_xml = f'<testsuite name="{test_suite_name}" tests="{len(self.test_files)}" failures="0" errors="0" time="0.0">'
                for line in result_file:
                    if 'Error' in line:
                        test_suite_xml += '<failure message="Test failed">' + line.strip().split(':')[1].strip() + '</failure>'
                        break
                test_suite_xml += '</testsuite>'
                test_suites_xml += test_suite_xml
                print(f'Results saved to: {result_file.name}')
            print('---')
    
class ParallelTestRunner(CommandRunner):
    def __init__(self, base_dir: str, python_path: str, num_processes: int):
        super().__init__(base_dir, python_path)
        self.num_processes = num_processes
        self.run_parallel_tests(num_processes)
        self.combine_results()
        self.generate_summary()
        self.generate_report_xml()

    def combine_results(self) -> None:
        combined_results_file = os.path.join(self.results_dir, 'combined_results.txt')
        with open(combined_results_file, 'w') as combined_results_file:
            combined_results_file.write('Combined test results:\n')
            combined_results_file.write(f'Python path: {self.python_path}\n')
            combined_results_file.write(f'Test files: {", ".join(self.test_files)}\n\n')
            for test_suite_name in self.test_suites:
                result_file = os.path.join(self.results_dir, f'{test_suite_name}.txt')
                with open(result_file, 'r') as result_file:
                    combined_results_file.write(result_file.read())
                    combined_results_file.write('\n---\n')
                    print(f'Results from test suite: {test_suite_name} combined.')
                    print(f'Results saved to: {combined_results_file.name}')
                    print('---')
    
    def generate_summary(self) -> None:
        summary_file = os.path.join(self.results_dir, 'summary.txt')
        with open(summary_file, 'w') as summary_file:
            summary_file.write('Test summary:\n')
            summary_file.write(f'Python path: {self.python_path}\n')
            summary_file.write(f'Test files: {", ".join(self.test_files)}\n\n')
            for test_suite_name in self.test_suites:
                result_file = os.path.join(self.results_dir, f'{test_suite_name}.txt')
                with open(result_file, 'r') as result_file:
                    result_lines = result_file.readlines()
                    passed_tests = sum(1 for line in result_lines if 'OK' in line)
                    failed_tests = sum(1 for line in result_lines if 'FAIL' in line)
                    skipped_tests = sum(1 for line in result_lines if 'SKIP' in line)
                    total_tests = len(result_lines)
                    summary_file.write(f'Test suite: {test_suite_name}\n')
                    summary_file.write(f'Passed: {passed_tests}\n')
                    summary_file.write(f'Failed: {failed_tests}\n')
                    summary_file.write(f'Skipped: {skipped_tests}\n')
                    summary_file.write(f'Total: {total_tests}\n\n')
                    print(f'Summary for test suite: {test_suite_name}')
                    print(f'Results saved to: {summary_file.name}')
                    print('---')
    
# Example usage
if __name__ == '__main__':
    base_dir = '/path/to/tests'
    python_path = '/path/to/python'
    num_processes = 4
    
    # Run tests in parallel
    parallel_runner = ParallelTestRunner(base_dir, python_path, num_processes)
    
    # Run tests sequentially
    sequential_runner = CommandRunner(base_dir, python_path)
    sequential_runner.run_tests()