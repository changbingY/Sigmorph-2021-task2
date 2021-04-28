import numpy as np
import scipy.spatial.distance

def load(fn):
    embedding = {}
    with open(fn, newline='') as f:
        for line in f:
            line = line.strip()
            if line:
                fields = line.split(" ")
                wf, vec = fields[0], fields[1:]
                embedding[wf] = np.array(vec, dtype=np.double)
    return embedding

def similarity(wf1,wf2,emb):
    return 1 - scipy.spatial.distance.cosine(emb[wf1], emb[wf2])

if __name__=="__main__":
    import sys
    emb = load(sys.argv[1])
    print(similarity("kaupunki","kaupungin",emb))
    print(similarity("kaupunki","koiralta",emb))
    print(similarity("kaupunki","se",emb))
