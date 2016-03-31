function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

if (!RedactorPlugins) var RedactorPlugins = {};

RedactorPlugins.icminline = function()
{
	return {
		init: function()
		{
			var that = this;
			var dropdown = {};

			dropdown.ltr = { title: 'Save', func: that.icminline.save };
			dropdown.rtl = { title: 'Close', func: that.icminline.cancel};

			var button = this.button.add('icminline-save', 'Save');
            this.button.setAwesome('icminline-save',	'fa-check-square-o');
            this.button.addCallback(button, this.icminline.save)
            button = this.button.add('icminline-cancel', 'Close');
            this.button.setAwesome('icminline-cancel',	'fa-times-circle');
            this.button.addCallback(button, this.icminline.cancel)
//			this.button.addDropdown(button, dropdown);
		},
		save: function()
		{
            console.log();
            data = {
                'otc': $(this.$editor).attr('id'),
                'content': this.code.get(),
                'csrfmiddlewaretoken': getCookie('csrftoken')
            };
            $.ajax({
              type: "POST",
              url: '/ajax/inline-save/',
              data: data,
              success: this.icminline.success
            });
		},
		cancel: function()
		{
			this.core.destroy()
		},
		success: function()
		{
			console.log('success')
		}
	};
};