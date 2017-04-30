/**
 * Created by yasser on 4/28/17.
 */
$(document).ready(function() {
    $('.rating')
        .rating({
            initialRating: 0,
            maxRating: 5
        })
    $('.rating')
        .rating('enable')
    $('.book.rating')
        .click(function () {
            var r = $(this).find(".active").length
            var id = this.id.split('_')[1]
            $.ajax({
                type: "POST",
                url: "/library/books/"+id+"/rating",
                data: {rating: r},
                success: function (data, status) {
                    console.log('book re-rated')
                }
            });
        })
    $('.author.rating')
        .click(function () {
            var r = $(this).find(".active").length
            var id = this.id.split('_')[1]
            $.ajax({
                type: "POST",
                url: "/library/authors/"+id+"/rating",
                data: {rating: r},
                success: function (data, status) {
                    console.log('author re-rated')
                }
            });
        })
})