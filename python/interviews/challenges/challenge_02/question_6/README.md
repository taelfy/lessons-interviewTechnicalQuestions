## Question 6.
### Create a CICD pipeline using the technology of your choice to deploy your code to production. 
Think about what stages might be required in a full CICD pipeline. Your code should be invokable from a public URL.

## Solution
- As per architecture diagram in ./question_1/README.md, Github Actions and Heroku used for CICD and Heroku used for hosting service.
  - Github Actions conducts testing and checks and "should" action PRs only to Preprod and Prod with approvals.
    - Dev work should also be done on a split branch from Preprod and merged in when ready.
  - A merge triggers the Heroku manifest and build into Preprod or Prod hosting.
- Public URLS:
  - https://challenge02-prod.herokuapp.com/
  - https://challenge02-preprod.herokuapp.com/
  - Payload format required same as question_3 test.

## Feedback
The CICD could be expanded on and built maybe more indepth.