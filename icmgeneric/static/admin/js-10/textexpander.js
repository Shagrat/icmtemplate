if (!RedactorPlugins) var RedactorPlugins = {};

RedactorPlugins.textexpander = function()
{
	return {
		items: [
			['lorem', 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'],
			['text', 'Text']
		],
		init: function()
		{
			this.$editor.on('keyup.redactor-limiter', $.proxy(function(e)
			{
				var key = e.which;
				if (key == this.keyCode.SPACE)
				{
					var current = this.selection.getCurrent();
					var cloned = $(current).clone();

					var $div = $('<div>');
					$div.html(cloned);

					var text = $div.html();
					$div.remove();

					var len = this.textexpander.items.length;
					var replaced = 0;

					for (var i = 0; i < len; i++)
					{
						var re = new RegExp(this.textexpander.items[i][0]);
						if (text.search(re) != -1)
						{
							replaced++;
							text = text.replace(re, this.textexpander.items[i][1]);

							$div = $('<div>');
							$div.html(text);
							$div.append(this.selection.getMarker());

							var html = $div.html().replace(/&nbsp;/, '');

							$(current).replaceWith(html);
							$div.remove();
						}
					}

					if (replaced !== 0)
					{
						this.selection.restore();
					}
				}


			}, this));

		}
	};
};