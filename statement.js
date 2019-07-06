$('pre code').each(function(i, e) {hljs.highlightBlock(e)});

var head = document.getElementsByTagName("head")[0], script;
script = document.createElement("script");
script.type = "text/x-mathjax-config";
script[(window.opera ? "innerHTML" : "text")] =
    "MathJax.Hub.Config({\n" +
    "  tex2jax: { inlineMath: [['$$$','$$$'], ['\\\\(','\\\\)']] }\n" +
    "});";
head.appendChild(script);
MathJax.Hub.Typeset()