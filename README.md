# MlOps Neuro - Model Deployment

Implemented -
1) Training model of character-level RNN to classify the words. The model was trained on a few thousand surnames from 18 languages of origin, and predicts which language a name is from based on the spelling. 
2) Bottle Python server as a REST API microservice running as a Docker container on the Neu.ro platform
3) API test job - Locust for Testing - Result and model saved in results folder

## Sign up
Sign up at [neu.ro](https://neu.ro) and setup your local machine using
 

```shell
pip install -U neuro-cli neuro-flow
neuro login
git clone https://github.com/ayushaggar/mlops-neuro-rnn
cd mlops-neuro-rnn
neuro-flow build myimage
neuro-flow upload ALL

```

For Training model
```

neuro-flow run train

```

For Serving model
```

neuro-flow run serve

```



Link depending on your neuro account will open in browser when you serve model

Then check predicted model  here - 
https://mlops-neuro-rnn-serve--ayushaggar.jobs.neuro-compute.org.neu.ro/predict/albert
where mlops-neuro-rnn is project name, serve is job name and ayushaggar is neuro account details

For Testing model and Serving locust

```

neuro-flow run locustrun

```

Link depending on your neuro account will open in browser when you run locustrun command

Then do testing here - 
https://mlops-neuro-rnn-locustrun--ayushaggar.jobs.neuro-compute.org.neu.ro/
where mlops-neuro-rnn is project name, locustrun is job name and ayushaggar is neuro account details


