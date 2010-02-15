$().ready( function () {
	$('textarea.tinymce').tinymce({
		script_url : '/static/js/tiny_mce/tiny_mce.js',
		theme : 'simple',
	});
});