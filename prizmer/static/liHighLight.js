$(function(){
    (function($){
    $.fn.liHighLight = function(params){
        var p = $.extend({
            words: '',
            class: 'highlight'
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
    $('.content').liHighLight({
        words:'Н/Д', 
        class: 'highlight'
    });
}); 