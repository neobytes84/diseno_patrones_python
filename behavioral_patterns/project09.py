# Behavioral patterns - State in Python -example 01
# Developed by Neobytes.io

import pandas as pd
import random
import datetime

class ReviewState:
    def __init__(self, name: str, review_score: int, review_date: datetime.date) -> None:
        self.name = name
        self.review_score = review_score
        self.review_date = review_date
    
    def __str__(self):
        return f"Reviewer: {self.name}\nReview Score: {self.review_score}\nReview Date: {self.review_date}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.review_score}, {self.review_date})"
    
    def approve(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def reject(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    def get_state(self) -> str:
        raise NotImplementedError("Subclasses must implement this method")
    def set_state(self, state: 'ReviewState'):
        raise NotImplementedError("Subclasses must implement this method")

class ApprovedState(ReviewState):
    def approve(self):
        print(f"{self.name}'s review has already been approved.")
    
    def reject(self):
        print(f"{self.name}'s review has been rejected.")
      
    
    def get_state(self) -> str:
        return "Approved"
    
    def set_state(self, state: 'ReviewState'):
        self.state = state
        print(f"State of {self.name}'s review has been set to {self.state}.")
    
    def update_score(self, new_score: int):
        self.review_score = new_score
        print(f"{self.name}'s review score has been updated to {self.review_score}.")
    
    def update_date(self, new_date: datetime.date):
        self.review_date = new_date
        print(f"{self.name}'s review date has been updated to {self.review_date}.")

class RejectedState(ReviewState):
    def approve(self):
        print(f"{self.name}'s review has been approved.")
    
    def reject(self):
        print(f"{self.name}'s review has already been rejected.")
    
    def get_state(self) -> str:
        return "Rejected"
    
    def set_state(self, state: 'ReviewState'):
        self.state = state
        print(f"State of {self.name}'s review has been set to {self.state}.")
    
    def update_score(self, new_score: int):
        self.review_score = new_score
        print(f"{self.name}'s review score has been updated to {self.review_score}.")
    
    def update_date(self, new_date: datetime.date):
        self.review_date = new_date
        print(f"{self.name}'s review date has been updated to {self.review_date}.")

class Review:
    def __init__(self, name: str, review_score: int, review_date: datetime.date) -> None:
        self.name = name
        self.review_score = review_score
        self.review_date = review_date
        self.state = RejectedState(name, review_score, review_date)
        self.previous_state = None
        self.history = []
    
    def __repr__(self):
        pass
    
    def approve(self):
        self.previous_state = self.state
        self.state.set_state(ApprovedState(self.name, self.review_score, self.review_date))
        self.history.append((datetime.datetime.now(), "Approved"))
    
    def reject(self):
        self.previous_state = self.state
        self.state.set_state(RejectedState(self.name, self.review_score, self.review_date))
        self.history.append((datetime.datetime.now(), "Rejected"))
    
    def update_score(self, new_score: int):
        self.state.update_score(new_score)
        self.history.append((datetime.datetime.now(), f"Updated score to {new_score}"))
        self.previous_state = self.state
        self.state = RejectedState(self.name, new_score, self.review_date)
        self.history.append((datetime.datetime.now(), "Updated to rejected state"))
        self.state.set_state(ApprovedState(self.name, new_score, self.review_date))
        self.history.append((datetime.datetime.now(), "Updated to approved state"))
        self.previous_state = self.state
        self.state = RejectedState(self.name, new_score, self.review_date)
        self.history.append((datetime.datetime.now(), "Updated to rejected state"))
    
    def update_date(self, new_date: datetime.date):
        self.state.update_date(new_date)
        self.history.append((datetime.datetime.now(), f"Updated date to {new_date}"))
        self.previous_state = self.state
        self.state = RejectedState(self.name, self.review_score, new_date)
        self.history.append((datetime.datetime.now(), "Updated to rejected state"))
        self.state.set_state(ApprovedState(self.name, self.review_score, new_date))
        self.history.append((datetime.datetime.now(), "Updated to approved state"))
        self.previous_state = self.state
        self.state = RejectedState(self.name, self.review_score, new_date)
        self.history.append((datetime.datetime.now(), "Updated to rejected state"))
        return self.history

# Test the implementation
if __name__ == "__main__":
    
    # Create a review object
    review = Review("John Doe", 90, datetime.date(2022, 1, 1))
    
    # Print the initial state
    print(f"Initial state: {review.state.get_state()}")
    
    # Approve the review
    review.approve()
    print(f"State after approval: {review.state.get_state()}")
    
    # Reject the review
    review.reject()
    print(f"State after rejection: {review.state.get_state()}")
    
    # Update the review score
    review.update_score(85)
    print(f"State after updating score: {review.state.get_state()}")
    
    # Update the review date
    review.update_date(datetime.date(2022, 2, 1))
    print(f"State after updating date: {review.state.get_state()}")
    print(f"Review history: {review.history}")
    print(f"Previous state: {review.previous_state.get_state()}")
    print(f"Current state: {review.state.get_state()}")
    print(f"Review score: {review.review_score}")
    print(f"Review date: {review.review_date}")
    print(f"Review name: {review.name}")
    print("---")