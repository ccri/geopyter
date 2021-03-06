import json

from geopyter.core.vis_gen.util.js_template_utility import append_div

def make(data, vis_params):
    uuid = vis_params['id']

    # first pass at axis control
    data_string = json.dumps(data)
    xVar = vis_params['x']
    yVar = vis_params['y']

    js_template = (
        "let data = " + data_string + ";"
        ""
        "requirejs(['nbextensions/d3.min'], function(d3) {"
        ""
        + append_div(uuid) +
        ""
        "let svg = d3.select('#" + uuid + "')"
        "    .append('svg')"
        "        .attr('viewBox', '0 0 960 480')"
        "        .attr('width', 960)"
        "        .attr('height', 480)"
        "        .attr('class', 'timeSeries');"
        ""
        "let mgn = {top:20, right:40, bottom:20, left:40};"
        "let wdt = svg.attr('width') - mgn.left - mgn.right;"
        "let hgt = svg.attr('height') - mgn.top - mgn.bottom;"
        "let g = svg.append('g')"
        "    .attr('transform', 'translate('+mgn.left+','+mgn.top+')');"
        ""
        "let parseDate = d3.timeParse('%Y-%m-%d');" # could be a parameter
        ""
        "let xScale = d3.scaleTime()"
        "    .domain(["
        "      d3.min(data, function(d) {"
        "        return parseDate(d." + xVar + ");"
        "      }),"
        "      d3.max(data, function(d) {"
        "        return parseDate(d." + xVar + ");"
        "      })"
        "    ])"
        "    .range([mgn.left, wdt]);"
        ""
        "let xAxis = d3.axisBottom(xScale)"
        "    .tickFormat(d3.timeFormat('%Y-%m-%d'));" # could be a parameter
        ""
        "let yScale = d3.scaleLinear()"
        "    .domain(["
        "      0,"
        "      d3.max(data, function(d) { return d." + yVar + "; })"
        "    ])"
        "    .range([hgt, mgn.bottom]);"
        ""
        "let yAxis = d3.axisLeft(yScale);"
        ""
        "g.append('g')"
        "    .attr('class', 'axis axis--x')"
        "    .attr('transform', 'translate(0,'+hgt+')')"
        "    .call(xAxis);"
        ""
        "g.append('g')"
        "    .attr('class', 'axis axis--y')"
        "    .call(yAxis);"
        ""
        "let bar = g.selectAll('.bar')"
        "    .data(data)"
        "    .enter().append('g')"
        "        .attr('class', 'bar');"
        ""
        "bar.append('rect')"
        "    .attr('class', 'databar')"
        "    .attr('x', function(d) {"
        "      return xScale(parseDate(d." + xVar + "));"
        "    })"
        "    .attr('y', function(d) { return yScale(d." + yVar + "); })"
        "    .attr('width', wdt / data.length)"
        "    .attr('height', function(d) {"
        "      return hgt - yScale(d." + yVar + ");"
        "    });"
        "});"
    )

    return ' '.join(js_template.split())