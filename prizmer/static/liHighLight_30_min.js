$(function(){
    (function($){
    $.fn.li30min = function(params){
        var p = $.extend({
            words: '',
            class: 'highlight_30'
        }, params);
        return this.each(function(){
            var wrap = $(this);
            var wArr = $.trim(p.words).split(' ');
            htmlreplace($(this));
            function htmlreplace(element){
                if (!element) element = document.body;
                var wrap = $(element).contents().each(function () {
                    if (this.nodeType === 3) {
                        var result = $(this).text();
                        for(i = 0; i < wArr.length; i++){
                            result = result.replace(new RegExp(wArr[i],'gi'),'<span class="'+p.class+'">$&</span>');
                        }
                        $(this).after(result).remove();
                    } else {
                        htmlreplace(this);
                    };
                });
            };
        });
    };
})(jQuery);
    $('.content').li30min({
        words:'48', 
        class: 'highlight_30'
    });
}); 