window.onload = function () {
    $.get('/get_hospital_mois', {}, function (data_return) {
        var m1 = data_return['M1'];
        var m2 = data_return['M2'];
        var m3 = data_return['M3'];
        var m4 = data_return['M4'];
        var m5 = data_return['M5'];
        var m6 = data_return['M6'];
        var m7 = data_return['M7'];
        var m8 = data_return['M8'];
        var m9 = data_return['M9'];
        var m10 = data_return['M10'];
        var m11 = data_return['M11'];
        var m12 = data_return['M12'];
        var x = new Chart(document.getElementById("chart_hospitalises"), {
            type: 'scatter',
            data: {
                datasets: [{label: "Les cas hospitalises par mois",data: [{x: 1,y: m1}, {x: 2,y: m2}, {x: 3,y: m3}, {x: 4,y: m4},
                {x: 5,y: m5}, {x: 6,y: m6}, {x: 7,y: m7}, {x: 8,y: m8},
                {x: 9,y: m9}, {x: 10,y: m10}, {x: 11,y: m11}, {x: 12,y: m12}],}]},
            options: {responsive: true}
        });

    })

}

$('#visualiser').click(function(){
    if ($('#name_graph').val()=='Nouvelles cas hospitalises'){
        $('#chart_cas_confirmes').hide();
        $('#chart_hospitalises').show();
        $.get('/get_hospital_mois', {}, function (data_return) {
        var m1 = data_return['M1'];
        var m2 = data_return['M2'];
        var m3 = data_return['M3'];
        var m4 = data_return['M4'];
        var m5 = data_return['M5'];
        var m6 = data_return['M6'];
        var m7 = data_return['M7'];
        var m8 = data_return['M8'];
        var m9 = data_return['M9'];
        var m10 = data_return['M10'];
        var m11 = data_return['M11'];
        var m12 = data_return['M12'];
        var x = new Chart(document.getElementById("chart_hospitalises"), {
            type: 'scatter',
            data: {
                datasets: [{label: "Les cas hospitalises par mois",data: [{x: 1,y: m1}, {x: 2,y: m2}, {x: 3,y: m3}, {x: 4,y: m4},
                {x: 5,y: m5}, {x: 6,y: m6}, {x: 7,y: m7}, {x: 8,y: m8},
                {x: 9,y: m9}, {x: 10,y: m10}, {x: 11,y: m11}, {x: 12,y: m12}],}]},
            options: {responsive: true}
        });

    })

    }
    else{
        $('#chart_hospitalises').hide();
        $('#chart_cas_confirmes').show();

        $.get('/get_nombre_confirmes', {}, function (data_return) {
        var m1 = data_return['M1'];
        var m2 = data_return['M2'];
        var m3 = data_return['M3'];
        var m4 = data_return['M4'];
        var m5 = data_return['M5'];
        var m6 = data_return['M6'];
        var m7 = data_return['M7'];
        var m8 = data_return['M8'];
        var m9 = data_return['M9'];
        var m10 = data_return['M10'];
        var m11 = data_return['M11'];
        var m12 = data_return['M12'];
        var x = new Chart(document.getElementById("chart_cas_confirmes"), {
            type: 'scatter',
            data: {
                datasets: [{label: "Les cas confirmés",data: [{x: 1,y: m1}, {x: 2,y: m2}, {x: 3,y: m3}, {x: 4,y: m4},
                {x: 5,y: m5}, {x: 6,y: m6}, {x: 7,y: m7}, {x: 8,y: m8},
                {x: 9,y: m9}, {x: 10,y: m10}, {x: 11,y: m11}, {x: 12,y: m12}],}]},
            options: {responsive: true}
        });

    })
    }
})