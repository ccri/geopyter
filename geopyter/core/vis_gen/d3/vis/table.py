import json

from geopyter.core.vis_gen.util.js_template_utility import append_div

def make(data, vis_params):
    uuid = vis_params['id']

    data_string = json.dumps(data)
    column_string = ','.join("'"+str(d)+"'" for d in data[0].keys())

    js_template = (
        "let data = " + data_string + ";"
        "let columns = [" + column_string + "];"
        ""
        "requirejs(['nbextensions/d3.min'], function(d3) {"
        ""
        + append_div(uuid) +
        ""
        "/* utility sorting functions */"
        "let stringCompare = function(a, b, ascending) {"
        "  a = a.toLowerCase();"
        "  b = b.toLowerCase();"
        "  if (!ascending)"
        "    return a > b ? -1 : a == b ? 0 : 1;"
        "  return a > b ? 1 : a == b ? 0 : -1;"
        "};"
        ""
        "let numberCompare = function(a, b, ascending) {"
        "  if (!ascending)"
        "    return a > b ? -1 : a == b ? 0 : 1;"
        "  return a > b ? 1 : a == b ? 0 : -1;"
        "};"
        ""
        "let table = d3.select('#" + uuid + "').append('table');"
        "let thead = table.append('thead');"
        "let tbody = table.append('tbody');"
        ""
        "let ascending = false;"
        ""
        "thead.append('tr')"
        "    .selectAll('th')"
        "    .data(columns)"
        "    .enter()"
        "    .append('th')"
        "        .text(function(column) { return column; })"
        "        .on('click', function(d) {"
        "          rows.sort(function(a, b) {"
        "            if (typeof a[d] == 'string')"
        "              return ((a === null || b === null)"
        "                ? 0 : stringCompare(a[d], b[d], ascending));"
        "            return ((a === null || b === null)"
        "              ? 0 : numberCompare(a[d], b[d], ascending));"
        "          });"
        "          ascending = !ascending;"
        "        });"
        ""
        "let rows = tbody.selectAll('tr')"
        "    .data(data)"
        "    .enter()"
        "    .append('tr');"
        ""
        "let cells = rows.selectAll('td')"
        "    .data(function(row) {"
        "      return columns.map(function(column) {"
        "        return {column: column, value: row[column]};"
        "      });"
        "    })"
        "    .enter()"
        "    .append('td')"
        "        .text(function(d) { return d.value; });"
        "});"
    )

    return ' '.join(js_template.split())