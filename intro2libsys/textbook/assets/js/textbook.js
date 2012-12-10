var Chapter = function(pages,pk,title) {
  this.pages = ko.observableArray(pages);
  this.pk = pk;
  this.title = title;
}

var Page = function(content,next_page,pk,prevous_page,title) {
  this.content = content;
  this.pk = pk;
  this.nextPage = ko.observable(next_page);
  this.previousPage = ko.observable(previous_page);
  this.title = ko.observable(title);
}

function GoToPage(page_pk) {
  textbook_view_model.loadPage(page_pk);
}

function TextbookPageViewModel() {
  // Data
  var self = this;
  self.currentPage = ko.observable();
  self.nextPage = ko.observable();
  self.pageContent = ko.observable();

 
  // Behaviours
  self.loadPage = function(page_id) {
    var data = "pk=" + page_id;
    $.ajax(
      {url: '/textbook/page',
       data: data,
       dataType: 'json',
       success: function(response) {
         self.pageContent(response.html);
         self.currentPage(response.title);
         if(!response.next) {
             self.nextPage(false);
         }
     }
   });    

  }

  self.previousPage = function() {
    alert("In previousPage " + location.hash);
  };
}
