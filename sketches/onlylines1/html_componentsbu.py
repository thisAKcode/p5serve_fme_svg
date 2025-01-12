html_beginning = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>FME Geometry</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/themes/prism.min.css">
  <script src="https://d3js.org/d3.v7.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/prism.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/prism/1.23.0/components/prism-python.min.js"></script>
  <script src="https://unpkg.com/htmx.org@1.6.1"></script>

<style>
      canvas {
      display: block;
      margin: auto;
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
      object-fit: contain;
    }
  @media (max-width: 600px) { 
    nav {
      margin: 0 auto 0.2em auto !important;
    }
  }
  body {
    display: flex !important;
    flex-direction: column !important;
    justify-content: flex-start !important;
    align-items: center !important;
  }
  main {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  svg {
    width: 100%;
    height: auto;
    margin: 0 auto;
    display: block;
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    background-color: #2d2d2d;
  }

  code {
    width: 100%;
    height: auto;
    margin: 0 auto;
    display: block;
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
    background-color: #2d2d2d;
    overflow-x: auto;
  }
  .token.operator {
    background: none !important;
  }
  #copy-button {
    display: block;
    margin: 20px auto;
    color: #f8f8f2;
    background-color: #2d2d2d;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
  }
  #code-block {
    color: #f8f8f2;
    background-color: #2d2d2d;
    text-shadow: none;
    display: block;
    white-space: pre;
    padding-left: 20px;
  }
  svg {
    padding: 5px 5px;

    margin: 20px auto;
  }
</style>
</head>


<body style="margin: 0; padding: 0; width: 100%; height: 100%; overflow-x: hidden;">
  <main id="index" class="home" style="margin-top: 0;">
    <header id="banner" class="body">
      <nav style="background: #000305; font-size: 1.143em; height: 40px; line-height: 30px; border-radius: 5px; -moz-border-radius: 5px; -webkit-border-radius: 5px;">
        <ul style="padding: 0; margin: 0; list-style: none;">
          <li style="float: left; display: inline; margin-right: 10px;"><a href="/" style="color: white; text-decoration: none;">Back to Blog</a></li>
          <li style="float: left; display: inline; margin-left: 10px;"><a href="/p5serve_fme_svg/index.html" style="color: white; text-decoration: none;">FME geometries</a></li>
        </ul>
      </nav>
    </header><!-- /#banner -->
  </main>

  <script>
    const projName = 'onlylines1'; // Replace with the actual project name
    const _filename = 'asset.svg'; // Replace with the actual filename
    const pathCheck = window.location.hostname === 'localhost' ? 'asset.svg' : `https://raw.githubusercontent.com/thisAKcode/p5serve_fme_svg/master/sketches/${projName}/${_filename}`;
    const svg = d3.select("body").append("svg")
      .attr("width", "70%")
      .attr("height", 500)
      .style("background-color", "#2d2d2d");

    d3.xml(pathCheck).then(data => {
      const importedNode = document.importNode(data.documentElement, true);
      svg.node().appendChild(importedNode);
      // Calculate dynamic stroke width based on canvas size
      const canvasWidth = svg.node().getBoundingClientRect().width;
      const dynamicStrokeWidth = canvasWidth * 0.001; // Adjust this factor as needed

      d3.selectAll("svg *")
        .style("stroke-width", dynamicStrokeWidth)
        .style("stroke", "white");
    });
  </script>


    


  <button id="copy-button">Copy Code</button>
"""

html_ending = """<script>
    document.getElementById('copy-button').addEventListener('click', function() {
      const codeBlock = document.getElementById('code-block');
      const range = document.createRange();
      range.selectNode(codeBlock);
      window.getSelection().removeAllRanges();
      window.getSelection().addRange(range);
      document.execCommand('copy');
      window.getSelection().removeAllRanges();
    });
  </script>
</body>
</html>
"""