$(function(){
  var margin = {top: 20, right: 50, bottom: 20, left: 50},
      width = 1200 - margin.right - margin.left,
      height = 1200 - margin.top - margin.bottom;
      
  var i = 0,
      duration = 750,
      root;

  var tree = d3.layout.tree()
      .size([height, width]);

  var diagonal = d3.svg.diagonal()
      .projection(function(d) { return [d.y, d.x]; });

  var svg = d3.select("#doc-to-graph").append("svg")
      .attr("width", width + margin.right + margin.left)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  d3.json("http://localhost:8080/generator.json", function(error, flare) {
    console.log(error, flare);
    root = flare;
    root.x0 = height / 2;
    root.y0 = 0;

    root.children.forEach(collapse);
    update(root);
  });

  function collapse(d, s) {
      if (d.children) {
      d._children = d.children;
      d._children.forEach(collapse);
      d.children = null;
    }
  }

  function collapseChild(d, s) {
    console.log(d);
    console.log(s);
      if (d.children) {
      d._children = d.children;
      d._children.forEach(collapse);
      d.children = null;
    }
  }

  d3.select(self.frameElement).style("height", "900px");

  var cR = 10;
  var headingStyle = "font-family: Arial;font-size : 13; /*stroke : #000000; */fill : #996633;";
  var contentStyle = "font-size : 11;";
  var tagStyle = "font-size : 11; fill: #D1684C;";
  var highStyle = "font-size : 11; fill: #48A197;";

  function update(source) {

    // Compute the new tree layout.
    var nodes = tree.nodes(root).reverse(),
        links = tree.links(nodes);
    // console.log(nodes);
    // console.log(links);

    // Normalize for fixed-depth.
    nodes.forEach(function(d) { d.y = d.depth * 180; });

    // Update the nodes…
    var node = svg.selectAll("g.node")
        .data(nodes, function(d) { return d.id || (d.id = ++i); });

    // Enter any new nodes at the parent's previous position.
    var nodeEnter = node.enter().append("g")
        .attr("class", "node")
        .attr("transform", function(d) { return "translate(" + source.y0 + "," + source.x0 + ")"; })
        .on("click", click);

    nodeEnter.append("circle")
        .attr("r", cR)
        .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

    nodeEnter.append("text")
        .attr("x", function(d) { return d.children || d._children ? -10 : 10; })
        .attr("dy", function(d) { return d.children || d._children ? ".3em" : ".75em"; })
        .attr("text-anchor", function(d) { return d.children || d._children ? "middle" : "start"; })
        .text(function(d) { return d.name; })
        .style("fill-opacity", 1e-6)
        .attr('style', function(d) { return d.children || d._children ? headingStyle : ""; })
        .call(wrap, function(d){return d;});

    // Transition nodes to their new position.
    var nodeUpdate = node.transition()
        .duration(duration)
        .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });

    nodeUpdate.select("circle")
        .attr("r", cR)
        .style("fill", function(d) { return d._children ? "lightsteelblue" : "#fff"; });

    nodeUpdate.select("text")
        .style("fill-opacity", 1);

    // Transition exiting nodes to the parent's new position.
    var nodeExit = node.exit().transition()
        .duration(duration)
        .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
        .remove();

    nodeExit.select("circle")
        .attr("r", cR);

    nodeExit.select("text")
        .style("fill-opacity", 1e-6);

    // Update the links…
    var link = svg.selectAll("path.link")
        .data(links, function(d) { return d.target.id; });

    // Enter any new links at the parent's previous position.
    link.enter().insert("path", "g")
        .attr("class", "link")
        .attr("d", function(d) {
          var o = {x: source.x0, y: source.y0};
          return diagonal({source: o, target: o});
        });

    // Transition links to their new position.
    link.transition()
        .duration(duration)
        .attr("d", diagonal);

    // Transition exiting nodes to the parent's new position.
    link.exit().transition()
        .duration(duration)
        .attr("d", function(d) {
          var o = {x: source.x, y: source.y};
          return diagonal({source: o, target: o});
        })
        .remove();

    // Stash the old positions for transition.
    nodes.forEach(function(d) {
      d.x0 = d.x;
      d.y0 = d.y;
    });
    
    // if (source.parent.children)
    //   source.parent.children.forEach(collapseChild);
  }

  // Toggle children on click.
  function click(d) {
    // console.log(d);
    if (d._children === null) {
      //console.log(d.parent);
    }
    if (d.children) {
      d._children = d.children;
      d.children = null;
    } else {
      d.children = d._children;
      d._children = null;
    }
    update(d);
  }

  function wrap(text) {
    var innerWidth = width/2;
    
    // console.log( this.children || this._children );
    text.each(function() {
      var text = d3.select(this),
          content = text.text(),
          words = content.split(/\s+/).reverse(),
          word,
          line = [],
          tags = [],
          lineNumber = 0,
          lineHeight = 0.5, // ems
          y = text.attr("y"),
          highlight = [],
          dy = parseFloat(text.attr("dy")),
          tspan = text.text(null)
            .append("tspan")
            .attr("x", 0)
            .attr("y", y)
            .attr('style', contentStyle)
            .attr("dx", dy + .3 + "em")
            .attr("dy", dy + "em");
      var data = text.data()[0] || {};
      // console.log(data);
      if (data.tags) {
        tags = data.tags.join(', ').split(/\s+/).reverse();
      }

      // if (data._children || data.children) {
      //   innerWidth = innerWidth / 1.5;
      // }
      if (data.summary) {
        var summarys = data.summary;
        var contentParts = [];
        for (var j = 0; j < summarys.length; j++) {
          summary = summarys[j];
          if (contentParts.length) {
            var temPart = [];
            for (var k = 0; k < contentParts.length; k++) {
              if (contentParts[k].type == "nonsummary") {
                var parts = contentParts[k].text.split(summary);
                for (var i = 0; i < parts.length; i++) {
                  temPart.push({text: parts[i].trim(), type: "nonsummary"});
                  if (parts[i+1]) {
                    temPart.push({text: summary, type: "summary"});
                  }
                };
              } else {
                temPart.push(contentParts[k]);
              }
            }
            contentParts = temPart;
            //var parts = content.split(summary);
          } else {
            var parts = content.split(summary);
            for (var i = 0; i < parts.length; i++) {
              contentParts.push({text: parts[i].trim(), type: "nonsummary"});
              if (parts[i+1]) {
                contentParts.push({text: summary, type: "summary"});
              }
            };
          }
        }
        for (var i = 0; i < contentParts.length; i++) {
          cp = contentParts[i];
          var con = cp.text.split(/\s+/).reverse();
          if (cp.type === 'nonsummary') {
            re = nonHighlightString(con, text, tspan, innerWidth, lineNumber, y, dy);
          } else {
            re = highlightString(con, text, tspan, innerWidth, lineNumber, y, dy);
          }
          tspan = re[0];
          text = re[1]
          lineNumber=re[2];
        }
      } else {
        re = nonHighlightString(words, text, tspan, innerWidth, lineNumber, y, dy, true);
        tspan = re[0];
        text = re[1]
        lineNumber=re[2];
      }


      var tagLine = [];
      if (tags.length > 0) {
        tspan = text.append("tspan")
            .attr("x", 0)
            .attr("y", y)
            .attr("dx", dy + .3 + "em")
            .attr("dy", lineHeight+dy+"em")
            .attr('style', tagStyle)
            .text('');
      }
      while (tag = tags.pop()) {
        tagLine.push(tag);
        tspan.text(tagLine.join(" "));
        if (tspan.node() && tspan.node().getComputedTextLength() > innerWidth) {
          tagLine.pop();
          tspan.text(tagLine.join(" "));
          tagLine = [tag];
          
          lineNumber = lineNumber + 1;
          tspan = text.append("tspan")
            .attr("x", 0)
            .attr("y", y)
            .attr("dx", dy + .3 + "em")
            .attr("dy", lineHeight+dy+"em")
            .attr('style', tagStyle)
            .text(tag);
        }
      }
    });
  }

  function nonHighlightString(words, text, tspan, innerWidth, lineNumber, y, dy, parent)
  {
      var line = [];
      var lineHeight = 0.5; // ems

      if (!parent) {
        tspan = text.append("tspan")
              .attr("x", 0)
              .attr("y", y)
              .attr("dx", dy + .3 + "em")
              .attr("dy", lineHeight+dy+"em")
              .attr('style', contentStyle)
              .text('');
      }

      while (word = words.pop()) {
        line.push(word);
        //console.log(line);
        tspan.text(line.join(" "));
        if (tspan.node().getComputedTextLength() > innerWidth) {
          line.pop();
          tspan.text(line.join(" "));
          line = [word];
          
          lineNumber = lineNumber + 1;
          tspan = text.append("tspan")
            .attr("x", 0)
            .attr("y", y)
            .attr("dx", dy + .3 + "em")
            .attr("dy", lineHeight+dy+"em")
            .attr('style', contentStyle)
            .text(word);

          //lineNumber = lineNumber + 1;
          //tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", lineNumber * lineHeight + dy + "em").text(word);
        }
      }
      return [tspan, text, lineNumber];
  }
  function highlightString(words, text, tspan, innerWidth, lineNumber, y, dy)
  {
      var line = [];
      var lineHeight = 0.5; // ems

      tspan = text.append("tspan")
            .attr("x", 0)
            .attr("y", y)
            .attr("dx", dy + .3 + "em")
            .attr("dy", lineHeight+dy+"em")
            .attr('style', highStyle)
            .text('');

      while (word = words.pop()) {
        line.push(word);
        //console.log(line);
        tspan.text(line.join(" "));
        if (tspan.node().getComputedTextLength() > innerWidth) {
          line.pop();
          tspan.text(line.join(" "));
          line = [word];
          
          lineNumber = lineNumber + 1;
          tspan = text.append("tspan")
            .attr("x", 0)
            .attr("y", y)
            .attr("dx", dy + .3 + "em")
            .attr("dy", lineHeight+dy+"em")
            .attr('style', highStyle)
            .text(word);

          //lineNumber = lineNumber + 1;
          //tspan = text.append("tspan").attr("x", 0).attr("y", y).attr("dy", lineNumber * lineHeight + dy + "em").text(word);
        }
      }
      return [tspan, text, lineNumber];
  }

});
