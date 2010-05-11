$().ready( function () {
	$('textarea.tinymce').tinymce({
		script_url : '/static/js/tiny_mce/tiny_mce.js',
		theme : 'advanced',
		theme_advanced_buttons1 : 'bold, italic, underline, strikethrough, separator,undo, redo, separator, cleanup, separator, link, unlink, image, separator, bullist, numlist, separator, outdent, indent, separator, blockquote, separator, code',
		theme_advanced_buttons2 : '',
		theme_advanced_buttons3 : '',

	});
});