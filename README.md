# Mlops Neuro RNN

## Sign up
Sign up at [neu.ro](https://neu.ro) and setup your local machine according to [instructions](https://docs.neu.ro/).
 
Then run:

```shell
pip install -U neuro-cli neuro-flow
neuro login
git clone https://github.com/ayushaggar/mlops-neuro-rnn
cd mlops-neuro-rnn
neuro-flow build myimage
neuro-flow upload ALL

```

```
For Training model
neuro-flow run train

```

```
For Serving model
neuro-flow run serve

```