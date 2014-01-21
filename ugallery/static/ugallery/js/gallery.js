
var ajax_req = null;
var base_url = $('#ugallery-load-more-photos').attr('href');

var load_more_images = function () {
    
    $('#ugallery-load-more-photos').click(function(event) {

        event.preventDefault();
        $('#ugallery-loader').show();
        var page = parseInt($('#ugallery-page').attr('data-page')) + 1;
        if (ajax_req == null) {
            ajax_req = $.get(base_url + page + '/');
            ajax_req.done(
                function(data) {
                    photos = $(data);
                    $.each(photos, function( index, value ) {                    
                        res = $("#ugallery-content").append(value);
                    });
                    $('#ugallery-page').attr('data-page', page);
                    $('#ugallery-load-more-photos').parent().show();
            }).fail(function() {
                $('#ugallery-load-more-photos').parent().remove();
            }).always(function() {
                $('#ugallery-loader').hide();   
                ajax_req = null;
            });
        }
    });
}


$("#ugallery-search-input").autocomplete({
    url: base_url + "search/",
    remoteDataType: 'json',
    selectFirst: true,
    minChars:1,
    onItemSelect: function(item) { 
        url = base_url + "tag/" + element.value.replace(" ", "-", 'g') + "/";
        window.location = url;
    }
});

var delete_photo = function(photo_id) {

    if (confirm('Are you sure to delete this photo?')) {
        $.post(base_url + 'photo/delete/' + photo_id + '/').done(
        function () {
            $('#ugallery-photo-container-' + photo_id).remove();    
        });


    }
    
};

$(document).ready(function() {
    load_more_images(); 
    $('#ugallery-load-more-photos').click();    
});