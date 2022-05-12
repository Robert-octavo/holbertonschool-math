<h1 class="gap">Math - LU Factorization</h1>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="LU Method" href="https://intranet.hbtn.io/rltoken/acIXjf6xYPmuHO6QA8ioeQ" target="_blank">LU Method</a></li>
<li><a title="LU Decomposition of a System of Linear Equations" href="https://intranet.hbtn.io/rltoken/S7sTWGSYXejCTBMzEfh_0g" target="_blank">LU Decomposition of a System of Linear Equations</a></li>
<li><a title="PLU decomposition" href="https://intranet.hbtn.io/rltoken/7_VZUU4kOandWsmHYNx9wA" target="_blank">PLU decomposition</a></li>
<li><a title="LU Decomposition--Computing Det(A)" href="https://intranet.hbtn.io/rltoken/wZ9WSgd2nC_IYvTmX2_OmA" target="_blank">LU Decomposition&ndash;Computing Det(A)</a></li>
<li><a title="Calculation of the determinant of a matrix using PLU" href="https://intranet.hbtn.io/rltoken/Z88nTXz8ef6ZWh9qjb8kPg" target="_blank">Calculation of the determinant of a matrix using PLU</a></li>
<li><a title="Iterative Methods" href="https://intranet.hbtn.io/rltoken/EHseFy9pjmXSJDHTiR5fuQ" target="_blank">Iterative Methods</a></li>
<li><a title="Descend gradient Method" href="https://intranet.hbtn.io/rltoken/VnPl_xtNHElMCkAdWG4neg" target="_blank">Descend gradient Method</a></li>
</ul>
<p><strong>References</strong>:</p>
<ul>
<li><a title="numpy.eye" href="https://intranet.hbtn.io/rltoken/L0M2WK1yX-kiN1ieoMMfDA" target="_blank">numpy.eye</a></li>
<li><a title="numpy.array" href="https://intranet.hbtn.io/rltoken/tnVy39UkZIgG94AqaTGhBA" target="_blank">numpy.array</a></li>
<li><a title="numpy.isclose" href="https://intranet.hbtn.io/rltoken/Fv-IcyC8-_X9IkUjegZ_uQ" target="_blank">numpy.isclose</a></li>
<li><a title="numpy.newaxis" href="https://intranet.hbtn.io/rltoken/b2TSdRR2DnDIVA5OsPhlXg" target="_blank">numpy.newaxis</a></li>
<li><a title="numpy.matmul" href="https://intranet.hbtn.io/rltoken/gsfVI19XSRvC2NSWURf4HA" target="_blank">numpy.matmul</a></li>
<li><a title="numpy.prod" href="https://intranet.hbtn.io/rltoken/4UaVUt7IeCGyKFIPBnmUSg" target="_blank">numpy.prod</a></li>
<li><a title="numpy.sum" href="https://intranet.hbtn.io/rltoken/f1b_Q0McFotPiDvgAOypLA" target="_blank">numpy.sum</a></li>
<li><a title="numpy.abs" href="https://intranet.hbtn.io/rltoken/qDuWcUqNsvUWChQ4p-_7OA" target="_blank">numpy.abs</a></li>
<li><a title="numpy.diag" href="https://intranet.hbtn.io/rltoken/anx8vqfG7t3His6redDR8Q" target="_blank">numpy.diag</a></li>
<li><a title="numpy.dot" href="https://intranet.hbtn.io/rltoken/l2sNXXYuHh8WNqp0ufObrw" target="_blank">numpy.dot</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/h3eiH4GqmpJU_D5r8FiXfA" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is LU decomposition?</li>
<li>What is PLU decomposition?</li>
<li>How to do LU decomposition?</li>
<li>How to do PLU decomposition?</li>
<li>How to find the calculate the determinant using PLU algorithm?</li>
<li>How to find the the gradient using the iterative method (descend gradient method)?</li>
</ul>
<h2>Requirements</h2>
<h3>Python Scripts</h3>
<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted/compiled on Ubuntu 20.04 LTS using <code>python3</code> (version 3.8)</li>
<li>Your files will be executed with <code>numpy</code></li>
<li>All your files should end with a new line</li>
<li>The first line of all your files should be exactly <code>#!/usr/bin/env python3</code></li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>Your code should follow pycodestyle (version <code>2.8.*</code>)</li>
<li>All your files must be executable</li>
</ul>
<h2>More Info</h2>
<h3>Installing pip (latest)</h3>
<p><a title="pip installation" href="https://intranet.hbtn.io/rltoken/aRq0XqU3NSgXFOCbOoq_XQ" target="_blank">pip installation</a></p>
<h3>Installing numpy</h3>
<pre><code>$ pip install numpy
</code></pre>
