<h1 class="gap">Math - Gauss elimination</h1>
<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2022/3/3a9a02e4a44393f77523169b2ba01fbacd55a04b.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220501%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20220501T045943Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=7410c62be3cd32d2bd0a4617d1aec48ef13a74ebfa4495c886b15f05bb3ad9d0" alt="" /></p>
<p>In this section we will show how mathematical approach can solve effectively some simple problems. We will solve the linear system Ax = b using Gauss elimination algorithm. We will return the inverse of a matrix using Gauss method.</p>
<h2>Resources</h2>
<p><strong>Read or watch</strong>:</p>
<ul>
<li><a title="Gauss Method" href="https://intranet.hbtn.io/rltoken/U-rtyP79giO7lLYK5RM60Q" target="_blank">Gauss Method</a></li>
<li><a title="Matrix inverse" href="https://intranet.hbtn.io/rltoken/lWXgYaO1s5LTyEjJk8dQhQ" target="_blank">Matrix inverse</a></li>
<li><a title="Computing inverse matrices using Gaussian elimination" href="https://intranet.hbtn.io/rltoken/l0SmHiC1PhD7DQUQg8YlLw" target="_blank">Computing inverse matrices using Gaussian elimination</a></li>
</ul>
<p><strong>References</strong>:</p>
<ul>
<li><a title="numpy.shape" href="https://intranet.hbtn.io/rltoken/5ZDFQsldHbYziYmDeJBbtA" target="_blank">numpy.shape</a></li>
<li><a title="numpy.concatenate" href="https://intranet.hbtn.io/rltoken/xEAd-bbnW4PtwpxJQ0_3eQ" target="_blank">numpy.concatenate</a></li>
<li><a title="numpy.argmax" href="https://intranet.hbtn.io/rltoken/RJDIn279TLEseXVVHDEamQ" target="_blank">numpy.argmax</a></li>
<li><a title="numpy.reshape" href="https://intranet.hbtn.io/rltoken/ObRE8ThPGN3VzzaYcx4i0w" target="_blank">numpy.reshape</a></li>
<li><a title="numpy.zeros" href="https://intranet.hbtn.io/rltoken/qQk6BQxhgSPv7amzy01LCg" target="_blank">numpy.zeros</a></li>
</ul>
<h2>Learning Objectives</h2>
<p>At the end of this project, you are expected to be able to <a title="explain to anyone" href="https://intranet.hbtn.io/rltoken/Uv_89QvrvAfqhRCQYU0F_g" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>
<h3>General</h3>
<ul>
<li>What is Guass elimination?</li>
<li>When you use Gauss elimination?</li>
<li>How to find the inverse of matrix using Gauss method?</li>
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
