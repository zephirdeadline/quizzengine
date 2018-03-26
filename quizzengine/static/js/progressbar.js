$(function() {
    $(".next").click(function () {

        var total = parseInt($('.questionnb').html());
        var nextValue = parseInt($('.progress-bar').attr('aria-valuenow'))+1;
        var valeur = Math.round(nextValue*100/total*100)/100;

        if (valeur > 100)
            valeur = 100;
        $('.progress-bar').css('width', valeur + '%').attr('aria-valuenow', nextValue);
        $('.bardisplay').text(valeur+"%")
    });

});