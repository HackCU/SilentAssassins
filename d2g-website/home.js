$('#graph').click(function() {
    if (!$(this).hasClass('active')) {
        $('#home').removeClass('active');
        $(this).addClass('active');
        $('.jumbotron').hide();
        $('#doc-to-graph').removeClass('hidden');
    }
    $('html, body').animate({
        scrollTop: ($("#doc-to-graph").offset().top + 150)
    }, 500);
});
$('#home').click(function() {
    if (!$(this).hasClass('active')) {
        $('#graph').removeClass('active');
        $(this).addClass('active');
        $('.jumbotron').show();
        $('#doc-to-graph').addClass('hidden');
    }
});
$('#intractive-graph').click(function(event) {
    $('#graph').trigger('click');
});