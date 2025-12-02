# Partial Dependence Plot (PDP) Summary

## Overview

Partial Dependence Plots (PDPs) are tools used in data science to
interpret complex machine learning models by illustrating how individual
features influence a model's predicted outcome.

## Example Scenario

A model is built for the NBA to predict whether a team will win its next
game based on: 
- Number of games won
- Number of games lost
- Number of injuries
- Total years of player experience

Stakeholders want to understand how each feature affects the predicted
probability of winning.

## How PDPs Are Created

1.  Select a feature (e.g., games won).
2.  Set that feature to a single value across all samples.
3.  Run the model and obtain predicted probabilities.
4.  Average those predictions to estimate the model's output for that
    feature value.
5.  Repeat this process for all possible values of the feature.
6.  Plot feature values (x-axis) vs. average predicted probabilities
    (y-axis).

## Advantages

-   Makes black-box models interpretable
-   Helps communicate model behavior to non-technical audiences
-   Supports trust and adoption of the model

## Major Limitations

### 1. Feature Independence Assumption

PDPs assume features are independent, which is often unrealistic.
Example: Wins + losses ≈ total games played.
Altering wins without adjusting losses can create impossible scenarios.

### 2. Averaging Hides Variation

PDPs display only the mean prediction, ignoring spread or uncertainty
across samples.

## Takeaway

PDPs are valuable interpretability tools but must be used with awareness
of their assumptions and limitations. They help data scientists explain
model logic---a crucial step for real-world implementation.

[Partial Dependence Plots (Opening the Black Box) - ritvikmath - youtube](https://www.youtube.com/watch?v=uQQa3wQgG_s)
