/**
 * Created by yasser on 4/28/17.
 */
$(function () {
    var frm = $(".author_follow")
    frm.submit(function(e){
        var author_id = frm.attr('id').split("_")[1]
        console.log(author_id)
        var my_case = $("input[name='case']", this)
        var btn_case = $("input[name='author']", this)
        console.log('sss')
        $.ajax({
            type: "POST",
            url:"/library/authors/"+author_id+"/follow",
            data: {'case':my_case.val()},
            success: function (data) {
                console.log(data)
                //style toggle
                if(data['done'] && data['case'] == "add" && btn_case.val() == "Follow") {
                    my_case.val("remove")
                    btn_case.val("Unfollow")
                    btn_case.toggleClass('red')
                }else if(data['done'] && data['case'] == "remove" && btn_case.val() == "Unfollow"){
                    my_case.val("add")
                    btn_case.val("Follow")
                    btn_case.toggleClass('red')
                }
            }
        })
        e.preventDefault()
    })
})