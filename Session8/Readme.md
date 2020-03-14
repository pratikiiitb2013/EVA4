<h2><i><b><font color='blue'>Session 8 Assignment</font></B></i></h2>
<hr>
<h3><i>Things to accomplish</i></h3>
<ol>
  <li>Use <b>Resnet 18</b> architecture and add it to API</li>
  <li>Use your data loader, model loading, train, and test code to train ResNet18 on <B>Cifar10</B></li>
  <li>Your Target is 85% accuracy. No limit on the number of epochs. Use default ResNet18 code (so params are fixed)</li>
</ol>
<hr>
<h3><i> FINAL Model Details</i></h3>
<ul>
  <li><B>Best Validation Accuracy</b>-88.77</li>
  <li><b>Epochs</b>-20</li>
  <li><b>Resnet18-parameters</b>- 11.174M</li>
  <li><b>Regularization</b>- Dropout(0.10), Augumentation(Flip,Rotate,ColorJitter), L2 Regularizer </li>
  <li><b>LR Optimizer</b>- MultiStepLR</li>
</ul>

<hr>
<h3><i>Model logs</i></h3>

```

0%|          | 0/391 [00:00<?, ?it/s]EPOCH: 1
Loss=1.0870977640151978 Batch_id=390 Accuracy=41.45: 100%|██████████| 391/391 [01:09<00:00,  6.22it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0101, Accuracy: 5448/10000 (54.48%)


EPOCH: 2
Loss=0.9237354397773743 Batch_id=390 Accuracy=58.65: 100%|██████████| 391/391 [01:09<00:00,  6.21it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0073, Accuracy: 6737/10000 (67.37%)


EPOCH: 3
Loss=0.6811982989311218 Batch_id=390 Accuracy=68.15: 100%|██████████| 391/391 [01:09<00:00,  6.21it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0063, Accuracy: 7344/10000 (73.44%)


EPOCH: 4
Loss=0.743315577507019 Batch_id=390 Accuracy=73.07: 100%|██████████| 391/391 [01:10<00:00,  6.26it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0052, Accuracy: 7721/10000 (77.21%)


EPOCH: 5
Loss=0.7581570744514465 Batch_id=390 Accuracy=76.29: 100%|██████████| 391/391 [01:10<00:00,  6.25it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0046, Accuracy: 8003/10000 (80.03%)


EPOCH: 6
Loss=0.7263234853744507 Batch_id=390 Accuracy=78.68: 100%|██████████| 391/391 [01:09<00:00,  6.27it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0049, Accuracy: 7852/10000 (78.52%)


EPOCH: 7
Loss=0.6407915353775024 Batch_id=390 Accuracy=80.63: 100%|██████████| 391/391 [01:09<00:00,  6.22it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0041, Accuracy: 8222/10000 (82.22%)


EPOCH: 8
Loss=0.4340116083621979 Batch_id=390 Accuracy=81.67: 100%|██████████| 391/391 [01:10<00:00,  6.28it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0040, Accuracy: 8289/10000 (82.89%)


EPOCH: 9
Loss=0.4963441491127014 Batch_id=390 Accuracy=83.00: 100%|██████████| 391/391 [01:10<00:00,  6.28it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0039, Accuracy: 8362/10000 (83.62%)


EPOCH: 10
Loss=0.4665961265563965 Batch_id=390 Accuracy=84.16: 100%|██████████| 391/391 [01:09<00:00,  6.25it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0038, Accuracy: 8340/10000 (83.40%)


EPOCH: 11
Loss=0.3297498822212219 Batch_id=390 Accuracy=85.17: 100%|██████████| 391/391 [01:10<00:00,  6.23it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0037, Accuracy: 8409/10000 (84.09%)


EPOCH: 12
Loss=0.5120591521263123 Batch_id=390 Accuracy=85.86: 100%|██████████| 391/391 [01:10<00:00,  6.27it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0037, Accuracy: 8467/10000 (84.67%)


EPOCH: 13
Loss=0.3424359858036041 Batch_id=390 Accuracy=86.84: 100%|██████████| 391/391 [01:09<00:00,  6.34it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0036, Accuracy: 8481/10000 (84.81%)


EPOCH: 14
Loss=0.2278444766998291 Batch_id=390 Accuracy=87.45: 100%|██████████| 391/391 [01:09<00:00,  6.24it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0036, Accuracy: 8456/10000 (84.56%)


EPOCH: 15
Loss=0.15181602537631989 Batch_id=390 Accuracy=90.71: 100%|██████████| 391/391 [01:09<00:00,  6.27it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0028, Accuracy: 8817/10000 (88.17%)


EPOCH: 16
Loss=0.18561486899852753 Batch_id=390 Accuracy=91.79: 100%|██████████| 391/391 [01:10<00:00,  6.27it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0027, Accuracy: 8843/10000 (88.43%)


EPOCH: 17
Loss=0.30170923471450806 Batch_id=390 Accuracy=92.33: 100%|██████████| 391/391 [01:09<00:00,  6.31it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0027, Accuracy: 8875/10000 (88.75%)


EPOCH: 18
Loss=0.2980807423591614 Batch_id=390 Accuracy=92.71: 100%|██████████| 391/391 [01:09<00:00,  6.26it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0027, Accuracy: 8877/10000 (88.77%)


EPOCH: 19
Loss=0.15129873156547546 Batch_id=390 Accuracy=93.08: 100%|██████████| 391/391 [01:10<00:00,  6.18it/s]
  0%|          | 0/391 [00:00<?, ?it/s]
Test set: Average loss: 0.0027, Accuracy: 8872/10000 (88.72%)


EPOCH: 20
Loss=0.23219139873981476 Batch_id=390 Accuracy=93.10: 100%|██████████| 391/391 [01:10<00:00,  6.24it/s]

Test set: Average loss: 0.0026, Accuracy: 8876/10000 (88.76%)


```
<hr>
<h3><i>Misclassified samples</i></h3>

![Image](https://github.com/pratikiiitb2013/EVA4/blob/master/Session8/EVA4S8_misclassified.png)

<hr>
Author - Pratik Jain
