# Sigmorph-2021-task2

## Embeddings

Fasttext embeddings compiled using the following command can be found in the directory `embeddings`:

```
./fasttext skipgram -input LAN.bible.txt -output ~/src/Sigmorph-2021-task2/embeddings/LAN.bible.txt -epoch 20 -minCount 1
```

You can load an embedding in the following way using `src/embeddings.py`:

```
>>> from embeddings import load
>>> emb = load("../embeddings/Spanish.bible.txt.vec")
>>> emb["hablar"]
array([ 1.6117e+00,  7.7046e-01,  1.1539e-01,  7.6902e-01, -2.5082e-01,
        1.1056e+00,  5.9999e-01,  1.3487e-01,  3.2986e-02,  2.6925e-01,
        3.2900e-01, -4.2670e-01, -4.0335e-01, -8.5261e-02, -1.0778e-01,
       -6.2948e-01,  8.8560e-02,  5.0664e-03,  1.9117e-01,  3.2212e-01,
       -4.6498e-01, -4.0603e-01,  6.0491e-01, -7.4713e-02, -5.0572e-03,
        6.8694e-01,  1.3701e+00,  9.5727e-02, -5.9283e-01,  5.1891e-01,
        1.5942e-03, -6.3309e-01, -7.9306e-01,  1.0360e-01, -7.8347e-02,
        3.9535e-01,  1.7196e-01,  5.2353e-01,  1.8521e-01,  3.8338e-01,
       -3.1244e-01, -2.4990e-01, -5.1462e-01,  3.8780e-01,  3.3233e-01,
        7.3420e-01, -6.0515e-02,  1.6242e-01,  5.2760e-01, -7.0372e-01,
       -4.1443e-03,  8.9978e-01,  3.4455e-01,  1.0276e+00, -4.3259e-01,
        7.6043e-01, -3.7236e-01,  9.3593e-02,  7.0134e-02, -4.7926e-01,
        2.0083e-01, -4.9352e-01,  4.2138e-01, -1.0336e-01, -2.0834e-01,
       -9.1329e-01, -7.0442e-01, -8.4698e-01,  7.6612e-03, -8.9519e-02,
       -2.7283e-02,  2.0751e-01,  5.5016e-01, -2.7888e-01,  1.8045e-02,
       -1.8576e-01, -1.8812e-01,  4.4698e-02,  2.0625e-01,  4.8604e-01,
        5.7186e-01, -3.8169e-01,  3.5239e-02,  4.8123e-01,  6.6832e-02,
       -3.8319e-02,  9.5217e-01, -1.7493e-01,  1.2172e-01, -2.3484e-01,
       -1.8055e-01,  9.0263e-01,  9.9269e-03,  1.7021e-01, -6.0385e-01,
       -8.9749e-02, -6.5046e-02,  1.0796e+00,  7.2462e-02, -1.9946e-01])
```

Embedding vectors can can be used as input for [`sklearn.cluste.KMeans`](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)


## Predictions

Codes and generated files of Prefix and Suffix rules systems and Discontinuous rules systems are in the directory `Predictions`:

You can use `prefix-suffix-rules.py` to generate results based on Prefix and Suffix rules. 

