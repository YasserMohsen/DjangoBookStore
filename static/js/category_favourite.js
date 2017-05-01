/**
 * Created by yasser on 4/28/17.
 */
$(function () {
    var frm = $(".category_fav")
    frm.submit(function(e){
        var cat_id = $(this).attr('id').split("_")[1]
        console.log(cat_id)
        var my_case = $("input[name='case']", this)
        var btn_case = $("input[name='category']", this)
        $.ajax({
            type: "POST",
            url:"/library/categorys/"+cat_id+"/favourites",
            data: {case:my_case.val()},
            success: function (data) {
                // console.log(data)
                //style toggle
                if(data['done'] && data['case'] == "add" && btn_case.val() == "Add To Favourites") {
                    my_case.val("remove")
                    btn_case.val("Remove From Favourites")
                    btn_case.toggleClass('red')
                }else if(data['done'] && data['case'] == "remove" && btn_case.val() == "Remove From Favourites"){
                    my_case.val("add")
                    btn_case.val("Add To Favourites")
                    btn_case.toggleClass('red')
                }
            }
        })
        e.preventDefault()
    })
})