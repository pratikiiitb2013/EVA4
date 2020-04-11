<h2><b><i> S11 Assignment</i></b></h2>
<hr>
<h3>Things to accomplish</h3>

```
1. Write code to find cyclic LR schedule and plot
2. Write code for custom resnet model(Details of model architecture on canvas page)
3. Uses One Cycle Policy such that:
   a. Total Epochs = 24
   b. Max at Epoch = 5
   c. LRMIN = FIND
   d. LRMAX = FIND
   e. NO Annihilation
4. Uses this transform -RandomCrop 32, 32 (after padding of 4) >> FlipLR >> Followed by CutOut(8, 8)
5. Batch size = 512
6. Target Accuracy: 90%
7. Make code more modular

```
<HR>
<h3>Cyclic LR schedule</h3>

![IMGAGE](https://github.com/pratikiiitb2013/EVA4/blob/master/Session11/cyclic_lr.png)

<HR>
<h3>LR range finder - accuracy vs LR curve</h3>

![IMGAGE](https://github.com/pratikiiitb2013/EVA4/blob/master/Session11/LR_range_finder.png)
<ul>
  <li>Trained model for 20 Epochs with linearly increasing LR between 1e-4 and 1</li>
  <li>Captures training accuracy at each LR value and plotted the above curve</li>
  <li>Resetted the model for each epoch(otherwise the max. training accuracy was coming in last epoch)</li>
  <li>max_lr = 0.05, min_lr = max_lr/10 = 0.005</li>
</ul>

<HR>
<h3>One cycle policy schedules for LR and momentum</h3>

![IMGAGE](https://github.com/pratikiiitb2013/EVA4/blob/master/Session11/OC_LR_momentum.png)
<ul>
  <li>Created one cycle schedule for LR(through values found shown above) and momentum</li>
  <li>Trained model for 24 epochs, with max_lr at 5th epoch</li>
</ul>

<HR>
<h3> Final Model metrics</h3>
<ul>
  <li>Epochs - 24</li>
  <li>Test accuracy - 91.40</li>
  <li>Augmentation - Albumentation (RandomCrop 32, 32 (after padding of 4) >> Horizontal Flip >> Followed by CutOut(8, 8))</li>
</ul>



<hr>

<h3>Training Logs</h3>


```
0%|          | 0/98 [00:00<?, ?it/s]EPOCH: 1
LR: [0.005272631578947369], M : [0.9500000000000001]
Loss=1.4652944803237915 Batch_id=97 Accuracy=35.16: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0029, Accuracy: 4937/10000 (49.37%)


EPOCH: 2
LR: [0.017136052631578948], M : [0.9125]
Loss=1.1091662645339966 Batch_id=97 Accuracy=53.60: 100%|██████████| 98/98 [00:23<00:00,  4.16it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0019, Accuracy: 6638/10000 (66.38%)


EPOCH: 3
LR: [0.028999473684210533], M : [0.875]
Loss=1.1294355392456055 Batch_id=97 Accuracy=62.46: 100%|██████████| 98/98 [00:23<00:00,  4.12it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0019, Accuracy: 6852/10000 (68.52%)


EPOCH: 4
LR: [0.04086289473684211], M : [0.8375]
Loss=0.7145311236381531 Batch_id=97 Accuracy=69.09: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0015, Accuracy: 7403/10000 (74.03%)


EPOCH: 5
LR: [0.05272631578947369], M : [0.8]
Loss=0.7967085242271423 Batch_id=97 Accuracy=74.24: 100%|██████████| 98/98 [00:23<00:00,  4.16it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0019, Accuracy: 6956/10000 (69.56%)


EPOCH: 6
LR: [0.05022875346260389], M : [0.8078947368421053]
Loss=0.7310501933097839 Batch_id=97 Accuracy=77.94: 100%|██████████| 98/98 [00:23<00:00,  4.15it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0013, Accuracy: 7816/10000 (78.16%)


EPOCH: 7
LR: [0.047731191135734076], M : [0.8157894736842105]
Loss=0.6421200633049011 Batch_id=97 Accuracy=81.21: 100%|██████████| 98/98 [00:23<00:00,  4.15it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0012, Accuracy: 7951/10000 (79.51%)


EPOCH: 8
LR: [0.04523362880886427], M : [0.8236842105263158]
Loss=0.39795583486557007 Batch_id=97 Accuracy=83.23: 100%|██████████| 98/98 [00:23<00:00,  4.10it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8427/10000 (84.27%)


EPOCH: 9
LR: [0.04273606648199446], M : [0.8315789473684211]
Loss=0.42075324058532715 Batch_id=97 Accuracy=85.16: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8418/10000 (84.18%)


EPOCH: 10
LR: [0.04023850415512466], M : [0.8394736842105264]
Loss=0.4312886595726013 Batch_id=97 Accuracy=86.04: 100%|██████████| 98/98 [00:23<00:00,  4.12it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8530/10000 (85.30%)


EPOCH: 11
LR: [0.037740941828254854], M : [0.8473684210526315]
Loss=0.4300054907798767 Batch_id=97 Accuracy=87.25: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8539/10000 (85.39%)


EPOCH: 12
LR: [0.03524337950138505], M : [0.8552631578947368]
Loss=0.38351044058799744 Batch_id=97 Accuracy=88.29: 100%|██████████| 98/98 [00:23<00:00,  4.15it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0009, Accuracy: 8494/10000 (84.94%)


EPOCH: 13
LR: [0.03274581717451524], M : [0.8631578947368421]
Loss=0.2681314945220947 Batch_id=97 Accuracy=89.12: 100%|██████████| 98/98 [00:23<00:00,  4.12it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0008, Accuracy: 8623/10000 (86.23%)


EPOCH: 14
LR: [0.03024825484764543], M : [0.8710526315789474]
Loss=0.29864954948425293 Batch_id=97 Accuracy=89.62: 100%|██████████| 98/98 [00:23<00:00,  4.13it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8802/10000 (88.02%)


EPOCH: 15
LR: [0.027750692520775624], M : [0.8789473684210526]
Loss=0.25436198711395264 Batch_id=97 Accuracy=90.63: 100%|██████████| 98/98 [00:23<00:00,  4.13it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8798/10000 (87.98%)


EPOCH: 16
LR: [0.02525313019390582], M : [0.8868421052631579]
Loss=0.25118035078048706 Batch_id=97 Accuracy=91.30: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8822/10000 (88.22%)


EPOCH: 17
LR: [0.022755567867036013], M : [0.8947368421052632]
Loss=0.18404552340507507 Batch_id=97 Accuracy=92.09: 100%|██████████| 98/98 [00:23<00:00,  4.15it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8902/10000 (89.02%)


EPOCH: 18
LR: [0.020258005540166206], M : [0.9026315789473686]
Loss=0.2687211334705353 Batch_id=97 Accuracy=92.53: 100%|██████████| 98/98 [00:23<00:00,  4.11it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8831/10000 (88.31%)


EPOCH: 19
LR: [0.017760443213296402], M : [0.9105263157894736]
Loss=0.26203274726867676 Batch_id=97 Accuracy=93.06: 100%|██████████| 98/98 [00:23<00:00,  4.12it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8924/10000 (89.24%)


EPOCH: 20
LR: [0.015262880886426591], M : [0.9184210526315789]
Loss=0.18281030654907227 Batch_id=97 Accuracy=93.79: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0007, Accuracy: 8956/10000 (89.56%)


EPOCH: 21
LR: [0.012765318559556788], M : [0.9263157894736842]
Loss=0.1150587722659111 Batch_id=97 Accuracy=94.52: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0006, Accuracy: 9010/10000 (90.10%)


EPOCH: 22
LR: [0.010267756232686984], M : [0.9342105263157895]
Loss=0.19184017181396484 Batch_id=97 Accuracy=95.07: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0006, Accuracy: 9065/10000 (90.65%)


EPOCH: 23
LR: [0.007770193905817173], M : [0.9421052631578948]
Loss=0.12220239639282227 Batch_id=97 Accuracy=95.62: 100%|██████████| 98/98 [00:23<00:00,  4.14it/s]
  0%|          | 0/98 [00:00<?, ?it/s]
Test set: Average loss: 0.0006, Accuracy: 9107/10000 (91.07%)


EPOCH: 24
LR: [0.005272631578947369], M : [0.9500000000000001]
Loss=0.10627087205648422 Batch_id=97 Accuracy=96.36: 100%|██████████| 98/98 [00:23<00:00,  4.13it/s]

Test set: Average loss: 0.0006, Accuracy: 9140/10000 (91.40%)

```

<HR>
Author - Pratik Jain



