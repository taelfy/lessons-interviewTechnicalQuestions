##Question 7
Document what components an enterprise machine learning system would have if you had the time to add it

What are some things that are critical to have versus nice to have?

##Answer
This project was done with all free services in a short amount of time. With proper time and enterprise level platforms, it would unlock much more services, increase robustness and be architectured with even better solutions and processes.

These notes are only a subsection of thought. There are plenty of other points to add but these are a few that come to mind.

Critical:
- Saving the model once model has finished development and benchmarks.
  - Save the model into a data storage or artifact zone. 
- Better and more logging in scripts.
- Alerting when critical issues arise and warnings for non-critical issues.
- More unit testing parts of the model process.
- Compare production/benchmark model to new models based on training set and QA data set.
- Get business user or process approval for new models before deploying to production.
- Standardised data and featuring engineering process pre-model.
- Model output saved to database, when applicable.
- Include more robust Architecture and Model monitoring and observability.
- Check updated new models load and speed.
- Update old "predictons" with new model predictions when applicable.

Nice-to-have:
- Batch testing the model.
- Model version control.
- Further model parameter, feature analysis and alternative model comparison and testing. E.g. try different process fo SGD, loss rate process, loss method or polynomial regression modelling.
- Hyperopts and SHAP to optimise models.
- Distributed data model processing.
- Proper microservice architecture integrated with other business services.
- Model ensemble when possible for higher accuracy.
- Model Devops tracking, e.g. staging to production.
- Model version, tags, metrics, parameters historisation for tracking.
- Proper declaration of Python function and define paramter types and return types.
- Check Model usage rate.
- Check model improvement or accuracy overtime.


For more enterprise CICD solutions, I'd consider improving the below:
- Better Auto CI testing on pull request and before merge.
- No pushes directly to infrastructure environments, e.g. Prod, Preprod. Pull requests only and approvals before merge.
- Preprod and Prod are critical, Dev is good to have. Branch splitting is critical for development, tracking, collaboration and version control.
- Using prefixes when deploying to either preprod or prod.