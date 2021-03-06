/* ===== Zeste de Savoir ====================================================
   Preview when editing news
   ========================================================================== */

(function($, undefined) {
    function updatePreview(data, element) {
        var $el = $(element);
        if(data.image) {
            $el.find(".featured-resource-illu").show().attr("src", data.image);
        }
        else {
            $el.find(".featured-resource-illu").hide();
        }

        $el.find("h3").text(data.title);
        $el.find(".featured-resource-description").html(data.description);
        $el.find("a").attr("href", data.link);
    }

    function buildDescription(_authors, type) {
        var authors = _authors.split(",");
        authors = authors.map($.trim);
        authors = authors.filter(function(e) { return e !== ""; });

        var text = type + " par ";
        authors.forEach(function(author, index) {
            text += "<i>" + author + "</i>";
            if(index === authors.length - 2) {
                text += " et ";
            } else if(index !== authors.length - 1) {
                text += ", ";
            }
        });
        return text;
    }

    $(".featured-resource-edit-form form input").on("change input", function() {
        updatePreview({
            image: $(".featured-resource-edit-form input[name=image_url]").val(),
            title: $(".featured-resource-edit-form input[name=title]").val(),
            description: buildDescription(
                $(".featured-resource-edit-form input[name=authors]").val(),
                $(".featured-resource-edit-form input[name=type]").val()
            ),
            link: $(".featured-edit-form input[name=url]").val(),
        }, $(".featured-resource-edit-form .featured-resource-item"));
    });
})(jQuery);
