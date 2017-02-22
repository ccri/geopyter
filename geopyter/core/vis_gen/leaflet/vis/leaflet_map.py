def make(data, vis_params):
    uuid = vis_params['id']

    js_template = (
        "requirejs(['nbextensions/leaflet'], function(L) {"
        ""
        "if (document.getElementById('" + uuid + "') === null)"
        "  element.append($('<div/>', {id:'" + uuid + "'}));"
        ""
        "let map = L.map('" + uuid + "').fitWorld();"
        "console.log(L);"
        "L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png').addTo(map);"

        "$(window).on('resize', function() {"
        "    $('#" + uuid + "').height($(window).height() / 2).width('100% - 14ex');"
        "    map.invalidateSize();"
        "}).trigger('resize');"

        # ""
        # ""
        # "let markers = [[37.5407, -77.4360], [38.0293, -78.4767]];"
        # "let layerGroup = L.layerGroup();"
        # "for (let coord of markers) {"
        # "  layerGroup.addLayer("
        # "      L.circle(coord, 500, {"
        # "          color: 'red',"
        # "          fillColor: '#f03',"
        # "          fillOpacity: 0.5"
        # "      })"
        # "  );"
        # "}"
        # "L.control.layers().addOverlay(layerGroup, 'test').addTo(map);"
        # ""
        # ""

        "});"
    )

    return ' '.join(js_template.split())