alert("I'm alive");
MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
$('pre code').each(function(i, e) {hljs.highlightBlock(e)});