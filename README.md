### Deploying on Heroku
* Create an `Heroku` app - `heroku create`.
* Push to `Heroku` master - `git push heroku master`.[1]
* Run app localy to see if it goes well.[4]
* As we are using a worker process[2], the process may not have been started 
automatically ( `web` process automatically starts when accessing the site 
). Scale the dynamo to start the process - `heroku ps:scale worker=1`[3]



[1]: https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app
[2]:https://devcenter.heroku.com/articles/process-model#mapping-the-unx-process-model-to-web-apps
[3]: https://devcenter.heroku.com/articles/procfile#scaling-a-process-type
[4]: https://devcenter.heroku.com/articles/heroku-local#run-your-app-locally-using-the-heroku-local-command-line-tool


