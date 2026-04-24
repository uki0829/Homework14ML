import matplotlib.pyplot as plt

from random import randint

class Homework04Utils():
  LABELS = ["florist", "forest", "tree"]
  L2I = {v:i for i,v in enumerate(LABELS)}

  @staticmethod
  def PRIME_SEED(i):
    return [3119, 3559, 3779][i]

  @staticmethod
  def plot_labels_vals(vls, title="Title"):
    l2v = {}
    for v,l in vls:
      label = l.split(".")[0].split("-")[0]
      l2v[label] = l2v.get(label, []) + [v]

    xs = l2v.values()
    ys = [len(v) * [i] for i,v in enumerate(xs)]

    plt.figure(figsize=(8, 2))
    plt.scatter(xs, ys)
    plt.yticks(range(0, len(l2v.keys())), list(l2v.keys()))
    plt.title(title)
    plt.show()

  @staticmethod
  def classification_accuracy(labels_and_filenames):
    preds = { l:[] for l in Homework04Utils.LABELS }
    acc = {}

    for label,fname in labels_and_filenames:
      correct_label = function(fname)
      preds[correct_label].append(label)

    for label, label_preds in preds.items():
      correct = [1 for pred in label_preds if pred == label]
      pct = 0 if len(label_preds) == 0 else sum(correct) / len(label_preds)
      acc[label] = round(pct, 5)

    acc["overall"] = round(sum(acc.values()) / len(acc.values()), 5)
    return acc

  @staticmethod
  def color_distance(c0, c1):
    return ((c0[0] - c1[0])**2 + (c0[1] - c1[1])**2 + (c0[2] - c1[2])**2) ** 0.5

  @staticmethod
  def color_ratio(pxs, keep_color, thold=150):
    filtcnt = [1 for rgb in pxs if Homework04Utils.color_distance(rgb, keep_color) < thold]
    return sum(filtcnt) / len(pxs)


def function(x):
  if "-" in x:
    return x.split("-")[0]
  else:
    x_int = int(x.split(".")[0])
    i_idx = [x_int % Homework04Utils.PRIME_SEED(i) == 0 for i in Homework04Utils.L2I.values()].index(True)
    return Homework04Utils.LABELS[i_idx]

def s2i(x):
  l = x.split("-")[0]
  i = int(x.split("-")[1].split(".")[0]) + 1
  return i * randint(1000, 3100) * Homework04Utils.PRIME_SEED(Homework04Utils.L2I[l])
