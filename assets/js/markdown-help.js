/* ===== Zeste de Savoir ====================================================
   Ugly markdown help block management
   TEMP : Add this to the future awesome Markdown editor directly
   ---------------------------------
   Author: Alex-D / Alexandre Demode
   ========================================================================== */

(function(document ,$, undefined){
    "use strict";

    $(".open-markdown-help").click(function(e){
        $(".markdown-help-more").toggleClass("show-markdown-help");

        var Text = $(".open-zen-mode").text();
        var TextToPut = $(".open-zen-mode").data("content-on-click");
        $(".open-zen-mode").data("content-on-click", Text);
        $(".open-zen-mode").text(TextToPut);

        e.preventDefault();
        e.stopPropagation();
    });
})(document, jQuery);