h2><i> Assignment 4 </i></h2>
<hr>

**ASSIGNMENT - Create an architecture using below conditions**<br>
<ul>
  <li>99.4% validation accuracy</li>
  <li>Less than 20k Parameters</li>
  <li>Less than 20 Epochs</li>
  <li>No fully connected layer</li>
</ul>

**Model Details**<br>
<ul>
  <li><B>EPOCHS</B> - 20</li>
  <li><B>PARAMETERS</B> - 19,580</li>
  <li><B>BEST TEST ACCURACY</B> - 99.53</li>
  <li><B> DROPOUT VALUE</B> - 0.1</li>
</UL>

**Architecture**<BR>
  
<B><I> (CONV2D+CONV2D) + POOLING + (CONV2D(1*1) + CONV2D + CONV2D) + POOLING + (CONV2D+CONV2D) + GAP + LOG_SOFTMAX</I></B><br>
No Bias used in CONV2D layers<br>

