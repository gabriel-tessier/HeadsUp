{% from "shared/_bootstrap_forms.html" import render_inline_field %}
line = '<br/>';
line += '<div id="reply_{{comment.id}}" class="well reply_form" >';
line += '	<p>{{ _('Reply to @%(name)s', name=comment.user.name) }}</p>';
line += '	<form action="{{url_for("reply_comment", post_id=postid, id=comment.id)}}" method="post" name="ReplyComment" autocomplete="off">';
line += '		{{form.hidden_tag()}}';
line += '		<div class="form-group"><textarea id="text_reply" name="body" placeholder="{{_('Your thoughts...')}}" rows="5"></textarea></div>';
line += '		<div class="buttons clearfix">';
line += '			<button id="btn_cancel" type="reset" class="btn btn-lg btn-tales-two">{{_('Cancel')}}</button>';
line += '			<button type="submit" class="btn btn-lg btn-tales-one pull-right">{{_('Submit')}}</button>';
line += '		</div>';
line += '	</form>';
line += '</div>';
$('.reply_form').remove();
$("#comment_{{comment.id}} .reply").html(line);
$('#reply_{{comment.id}} #text_reply').ckeditor();
$('#reply_{{comment.id}} #btn_cancel').click(function(){
	$("#comment_{{comment.id}} .reply").html('');
	return false;
});
