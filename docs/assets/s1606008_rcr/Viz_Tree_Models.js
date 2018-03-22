
function main_tree() {
    
    var widthTree=960;
    var heightTree=1060;

    var svg = d3.select("#chart_tree").append("svg:svg")
        .attr("width", widthTree)
        .attr("height", heightTree)
        .attr("id", "radialTree_Models")
        g = svg.append("g").attr("transform", "translate(" + (widthTree / 2 + 40) + "," + (heightTree / 2 + 90) + ")");

    var tree = d3.tree()
        .size([2 * Math.PI, 300])
        .separation(function(a, b) { return (a.parent == b.parent ? 1 : 2) / a.depth; });

    //method creating the sunburst diagram
    d3.json("/PluginsDocumentation/assets/s1606008_rcr/flare_4.json", function (error, root) {
        if (error) throw error;
        var jsonNodes = getModelNode(root.children)
        //create tree visualization
        createVisualizationTree(jsonNodes, tree, g);
});
}

//setting up d3 Tree
function createVisualizationTree(json, tree, g) {

    //only select the first child node () the first 
    var root = tree(d3.hierarchy(json.children[0]));

    var link = g.selectAll(".link")
        .data(root.links())
        .enter().append("path")
            .attr("class", "link")
            .attr("d", d3.linkRadial()
            .angle(function(d) { return d.x; })
            .radius(function(d) { return d.y; }));

    var node = g.selectAll(".node")
        .data(root.descendants())
        .enter().append("g")
            .attr("class", function(d) { return "node" + (d.children ? " node--internal" : " node--leaf"); })
            .attr("transform", function(d) { return "translate(" + radialPoint(d.x, d.y) + ")"; });
            
    //add data
    node.append("title")
        .text(function (d) { return d.data.name; });
    node.append("id")
        .text(function (d) { return d.data.Id; });

    //bigger node circle for internal nodes
    node.append("circle")
        .attr("r", function(d) { return (d.children ? 3.5 :2.5); })
    //text for nodes with children
    node.filter(function(d) { return d.children; })
        .append("text")
        .attr("dy", "0.4em")//offset to make space for name only
        .attr("x", function(d) { return d.x < Math.PI === !d.children ? 6 : -6; })
        .attr("text-anchor", function(d) { return d.x < Math.PI === !d.children ? "start" : "end"; })
        .attr("transform", function(d) { return "rotate(" + (d.x < Math.PI ? d.x - Math.PI / 2 : d.x + Math.PI / 2) * 180 / Math.PI + ")"; })
        .text(function(d) { 
            //return d.data.name ? d.data.name + " " + d.data.Id : d.data.Id; 
            return d.data.Id;
        });
    //text for leave nodes
    node.filter(function(d) { return !d.children; })
        .append("text")
        .attr("dy", "0.45em")//offset to make space for name only
        .attr("x", function(d) { return d.x < Math.PI === !d.children ? 6 : -6; })
        .style("stroke", function(d){ return getColourByModelType(d.data.name)} )
        .attr("text-anchor", function(d) { return d.x < Math.PI === !d.children ? "start" : "end"; })
        .attr("transform", function(d) { return "rotate(" + (d.x < Math.PI ? d.x - Math.PI / 2 : d.x + Math.PI / 2) * 180 / Math.PI + ")"; })
        .text(function(d) { 
            //return d.data.name ? d.data.name + " " + d.data.Id : d.data.Id; 
            return d.data.name;
        });

        node.filter(function(d) { return !d.children; })
        .append("text")
        .attr("dy", "-0.45em")//offset to make space for name only
        .attr("x", function(d) { return d.x < Math.PI === !d.children ? 6 : -6; })
        .style("stroke", function(d){ return getColourByModelType(d.data.name)} )
        .attr("text-anchor", function(d) { return d.x < Math.PI === !d.children ? "start" : "end"; })
        .attr("transform", function(d) { return "rotate(" + (d.x < Math.PI ? d.x - Math.PI / 2 : d.x + Math.PI / 2) * 180 / Math.PI + ")"; })
        .text(function(d) { 
            //return d.data.name ? d.data.name + " " + d.data.Id : d.data.Id; 
            return d.data.Id;
        });
}

//-----------------------------------------
//utility functions
//-----------------------------------------
function radialPoint(x, y) {
    return [(y = +y) * Math.cos(x -= Math.PI / 2), y * Math.sin(x)];
}

//function just returning the models node
function getModelNode(arr) {
    match = false;
    for (var i = 0; i < arr.length; i++)
    {
        if  (arr[i].Id === "MOD")
        {
            return arr[i];
        }
    }
    if (match==false)
    {
        for (var i = 0; i < arr.length; i++)
        {
            if (Array.isArray(arr[i].children))
            {
                return getModelNode(arr[i].children);
            }
        }
    }
}

function getColourByModelType(name)
{
    var colors = {
        "other": "#bbbbbb",
        "Revit": "#2c7fb8",
        "NavisWorks" : "#2ca25f"
    };
    return colors[getModelTypeByName(name)];
}

function getModelTypeByName (name)
{
    if (name.toLowerCase().indexOf("revit")>=0)
    {
        return ("Revit");
    }
    else if(name.toLowerCase().indexOf("nwd")>=0 || name.toLowerCase().indexOf("nwc")>=0 || name.toLowerCase().indexOf("nwf")>=0)
    {
        return "NavisWorks";
    }
    else  
    {
        return "other";
    }
}

//caller
main_tree();
