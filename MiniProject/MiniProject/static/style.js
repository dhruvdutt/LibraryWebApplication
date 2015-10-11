$(document).ready(function () {
    $(".button-collapse").sideNav();
})
$('#id').keydown(function (e) {
    if (e.which == 9 || e.which == 13) {
        e.preventDefault();
        var id = $('#id').val();
        $.ajax({
            type: "POST",
            url: "/updatebook",
            data: {id: id },
            success: function (responce) {
                $('#uname').val(responce.bookname);
                $('#uauthor').val(responce.author);
                $('#upublisher').val(responce.publisher);
                $('#udate').val(responce.date);
                $('#uprice').val(responce.price);
                $('#ucd').val(responce.cd);
                $('#ustatus').val(responce.status);
            }
        });
    }
});

$('#updatebook').submit(function (e) {
    e.preventDefault();
    var id = $('#bookid').val();
    var name = $('#bookname').val();
    var author = $('#author').val();
    var publisher = $('#publisher').val();
    var date = $('#date').val();
    var price = $('#price').val();
    var cd = $('#cd').val();
    var status = $('#status').val();
    $.ajax({
        type: "POST",
        url: "/update",
        data: { bookid: id, bookname: name, author: author, publisher: publisher, date: date, price: price, cd: cd, status: status },
        success: function (responce) {
            if (responce.responce == 1) {
                $('#responce').css({ color: 'green' });
                $('#responce').html("Record Updated Successfully");
            }
            else {
                console.log(responce);
            }
        }
    });
})

$('#roll').keyup(function () {
    var search = $('#roll').val();
    $.ajax({
        type: "POST",
        url: "/search",
        data: { search : search },
        success: function (response) {
            $("#roll").autocomplete({
                source: response
            });
        }
    });
})