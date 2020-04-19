<h2><i> Assignment A </I></h2>
<hr>

<h3><i> Task to accomplish </I></h3>

```
Assignment B:
1) Download this TINY IMAGENET (Links to an external site.) dataset. 
2) Train ResNet18 on this dataset (70/30 split) for 50 Epochs. Target 50%+ Validation Accuracy. 
3) Submit Results. Of course, you are using your own package for everything. You can look at this (Links to an external site.) for  reference. 

```
<HR>
<h3>One cycle policy schedules for LR and momentum</h3>

![IMGAGE](https://github.com/pratikiiitb2013/EVA4/blob/master/Session11/OC_LR_momentum.png)
<ul>
  <li>Created one cycle schedule for LR(through values found shown above) and momentum</li>
  <li>Trained model for 24 epochs, with max_lr at 5th epoch</li>
</ul>

<HR>
  
<h3><i> LOGS </I></h3>

```
 0%|          | 0/301 [00:00<?, ?it/s]
EPOCH: 1
LR: [0.010499999999999999], M : [0.9500000000000001]
Loss=4.011697769165039 Batch_id=300 Accuracy=6.92: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0175, Accuracy: 3039/33000 (9.21%)


EPOCH: 2
LR: [0.020999999999999998], M : [0.9333333333333333]
Loss=3.6050870418548584 Batch_id=300 Accuracy=14.79: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0159, Accuracy: 4550/33000 (13.79%)


EPOCH: 3
LR: [0.0315], M : [0.9166666666666665]
Loss=3.206441640853882 Batch_id=300 Accuracy=20.93: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0135, Accuracy: 7287/33000 (22.08%)


EPOCH: 4
LR: [0.041999999999999996], M : [0.9]
Loss=3.4332873821258545 Batch_id=300 Accuracy=26.00: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0136, Accuracy: 7373/33000 (22.34%)


EPOCH: 5
LR: [0.052500000000000005], M : [0.8833333333333333]
Loss=3.1355698108673096 Batch_id=300 Accuracy=30.02: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0136, Accuracy: 7663/33000 (23.22%)


EPOCH: 6
LR: [0.063], M : [0.8666666666666667]
Loss=2.6610660552978516 Batch_id=300 Accuracy=33.20: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0118, Accuracy: 9700/33000 (29.39%)


EPOCH: 7
LR: [0.0735], M : [0.85]
Loss=2.572067975997925 Batch_id=300 Accuracy=36.04: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0113, Accuracy: 10586/33000 (32.08%)


EPOCH: 8
LR: [0.084], M : [0.8333333333333334]
Loss=2.3879714012145996 Batch_id=300 Accuracy=38.46: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0116, Accuracy: 10301/33000 (31.22%)


EPOCH: 9
LR: [0.0945], M : [0.8166666666666667]
Loss=2.46943736076355 Batch_id=300 Accuracy=40.96: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0112, Accuracy: 10942/33000 (33.16%)


EPOCH: 10
LR: [0.10499999999999998], M : [0.8]
Loss=2.113075017929077 Batch_id=300 Accuracy=43.02: 100%|██████████| 301/301 [02:38<00:00,  1.90it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0106, Accuracy: 11751/33000 (35.61%)


EPOCH: 11
LR: [0.10185], M : [0.805]
Loss=2.024372100830078 Batch_id=300 Accuracy=44.86: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0112, Accuracy: 11242/33000 (34.07%)


EPOCH: 12
LR: [0.0987], M : [0.81]
Loss=2.1989073753356934 Batch_id=300 Accuracy=46.17: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0100, Accuracy: 12662/33000 (38.37%)


EPOCH: 13
LR: [0.09555], M : [0.8150000000000001]
Loss=2.195202589035034 Batch_id=300 Accuracy=47.57: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0100, Accuracy: 13038/33000 (39.51%)


EPOCH: 14
LR: [0.0924], M : [0.8200000000000001]
Loss=2.280269145965576 Batch_id=300 Accuracy=48.83: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0107, Accuracy: 12126/33000 (36.75%)


EPOCH: 15
LR: [0.08925], M : [0.8250000000000001]
Loss=2.0309832096099854 Batch_id=300 Accuracy=49.79: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0109, Accuracy: 12044/33000 (36.50%)


EPOCH: 16
LR: [0.0861], M : [0.8300000000000001]
Loss=1.9973206520080566 Batch_id=300 Accuracy=50.95: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0107, Accuracy: 12299/33000 (37.27%)


EPOCH: 17
LR: [0.08295], M : [0.835]
Loss=1.9708071947097778 Batch_id=300 Accuracy=51.96: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0127, Accuracy: 10105/33000 (30.62%)


EPOCH: 18
LR: [0.0798], M : [0.84]
Loss=2.195077896118164 Batch_id=300 Accuracy=52.92: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0102, Accuracy: 12993/33000 (39.37%)


EPOCH: 19
LR: [0.07665], M : [0.845]
Loss=1.8594412803649902 Batch_id=300 Accuracy=53.94: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0090, Accuracy: 14661/33000 (44.43%)


EPOCH: 20
LR: [0.0735], M : [0.85]
Loss=1.7533023357391357 Batch_id=300 Accuracy=54.46: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0096, Accuracy: 13643/33000 (41.34%)


EPOCH: 21
LR: [0.07035], M : [0.855]
Loss=1.7709016799926758 Batch_id=300 Accuracy=55.36: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0093, Accuracy: 14220/33000 (43.09%)


EPOCH: 22
LR: [0.0672], M : [0.86]
Loss=1.6704208850860596 Batch_id=300 Accuracy=56.05: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0092, Accuracy: 14495/33000 (43.92%)


EPOCH: 23
LR: [0.06405], M : [0.865]
Loss=1.6938008069992065 Batch_id=300 Accuracy=57.15: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0096, Accuracy: 13784/33000 (41.77%)


EPOCH: 24
LR: [0.06089999999999999], M : [0.87]
Loss=1.8499118089675903 Batch_id=300 Accuracy=57.66: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0096, Accuracy: 14004/33000 (42.44%)


EPOCH: 25
LR: [0.057749999999999996], M : [0.875]
Loss=1.8683404922485352 Batch_id=300 Accuracy=58.06: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0095, Accuracy: 14089/33000 (42.69%)


EPOCH: 26
LR: [0.054599999999999996], M : [0.88]
Loss=1.5838534832000732 Batch_id=300 Accuracy=59.22: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0098, Accuracy: 13973/33000 (42.34%)


EPOCH: 27
LR: [0.051449999999999996], M : [0.885]
Loss=1.647720217704773 Batch_id=300 Accuracy=59.78: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0096, Accuracy: 14134/33000 (42.83%)


EPOCH: 28
LR: [0.048299999999999996], M : [0.89]
Loss=1.4746153354644775 Batch_id=300 Accuracy=60.64: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0085, Accuracy: 15733/33000 (47.68%)


EPOCH: 29
LR: [0.045149999999999996], M : [0.895]
Loss=1.6321007013320923 Batch_id=300 Accuracy=60.95: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0089, Accuracy: 15303/33000 (46.37%)


EPOCH: 30
LR: [0.041999999999999996], M : [0.9]
Loss=1.3705068826675415 Batch_id=300 Accuracy=62.02: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0088, Accuracy: 15441/33000 (46.79%)


EPOCH: 31
LR: [0.038849999999999996], M : [0.905]
Loss=1.6669427156448364 Batch_id=300 Accuracy=62.94: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0093, Accuracy: 15019/33000 (45.51%)


EPOCH: 32
LR: [0.035699999999999996], M : [0.91]
Loss=1.269659399986267 Batch_id=300 Accuracy=63.70: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0084, Accuracy: 16140/33000 (48.91%)


EPOCH: 33
LR: [0.032549999999999996], M : [0.9149999999999999]
Loss=1.215968370437622 Batch_id=300 Accuracy=65.05: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0090, Accuracy: 15378/33000 (46.60%)


EPOCH: 34
LR: [0.029399999999999996], M : [0.9199999999999999]
Loss=1.320934772491455 Batch_id=300 Accuracy=65.65: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0088, Accuracy: 15764/33000 (47.77%)


EPOCH: 35
LR: [0.026249999999999996], M : [0.9249999999999999]
Loss=1.5038249492645264 Batch_id=300 Accuracy=67.11: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0083, Accuracy: 16563/33000 (50.19%)


EPOCH: 36
LR: [0.023099999999999996], M : [0.9299999999999999]
Loss=1.2713158130645752 Batch_id=300 Accuracy=68.29: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0085, Accuracy: 16223/33000 (49.16%)


EPOCH: 37
LR: [0.019949999999999996], M : [0.9349999999999999]
Loss=1.3305259943008423 Batch_id=300 Accuracy=70.00: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0080, Accuracy: 17080/33000 (51.76%)


EPOCH: 38
LR: [0.016799999999999995], M : [0.9399999999999998]
Loss=1.257417917251587 Batch_id=300 Accuracy=72.00: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0076, Accuracy: 17685/33000 (53.59%)


EPOCH: 39
LR: [0.013649999999999995], M : [0.9449999999999998]
Loss=1.133540153503418 Batch_id=300 Accuracy=74.54: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0076, Accuracy: 17876/33000 (54.17%)


EPOCH: 40
LR: [0.010499999999999999], M : [0.9500000000000001]
Loss=1.1122924089431763 Batch_id=300 Accuracy=77.66: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0077, Accuracy: 17885/33000 (54.20%)


EPOCH: 41
LR: [0.009545454545454544], M : [0.9500000000000001]
Loss=0.8537760376930237 Batch_id=300 Accuracy=80.07: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0077, Accuracy: 17925/33000 (54.32%)


EPOCH: 42
LR: [0.00859090909090909], M : [0.9500000000000001]
Loss=0.7503109574317932 Batch_id=300 Accuracy=82.09: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0075, Accuracy: 18257/33000 (55.32%)


EPOCH: 43
LR: [0.007636363636363636], M : [0.9500000000000001]
Loss=0.6849406957626343 Batch_id=300 Accuracy=84.36: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0074, Accuracy: 18659/33000 (56.54%)


EPOCH: 44
LR: [0.006681818181818181], M : [0.9500000000000001]
Loss=0.49236124753952026 Batch_id=300 Accuracy=86.99: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0073, Accuracy: 18931/33000 (57.37%)


EPOCH: 45
LR: [0.005727272727272727], M : [0.9500000000000001]
Loss=0.6133456230163574 Batch_id=300 Accuracy=89.68: 100%|██████████| 301/301 [02:38<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0070, Accuracy: 19240/33000 (58.30%)


EPOCH: 46
LR: [0.004772727272727272], M : [0.9500000000000001]
Loss=0.44133761525154114 Batch_id=300 Accuracy=91.91: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0068, Accuracy: 19632/33000 (59.49%)


EPOCH: 47
LR: [0.003818181818181818], M : [0.9500000000000001]
Loss=0.3376089930534363 Batch_id=300 Accuracy=94.43: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0066, Accuracy: 20088/33000 (60.87%)


EPOCH: 48
LR: [0.0028636363636363633], M : [0.9500000000000001]
Loss=0.26322081685066223 Batch_id=300 Accuracy=96.34: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0064, Accuracy: 20334/33000 (61.62%)


EPOCH: 49
LR: [0.001909090909090909], M : [0.9500000000000001]
Loss=0.18843168020248413 Batch_id=300 Accuracy=97.60: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
  0%|          | 0/301 [00:00<?, ?it/s]
Test set: Average loss: 0.0064, Accuracy: 20519/33000 (62.18%)


EPOCH: 50
LR: [0.0009545454545454544], M : [0.9500000000000001]
Loss=0.17888356745243073 Batch_id=300 Accuracy=98.37: 100%|██████████| 301/301 [02:39<00:00,  1.89it/s]
Test set: Average loss: 0.0063, Accuracy: 20659/33000 (62.60%)

```

Group members - Siddharth Surange, Pratik Jain

