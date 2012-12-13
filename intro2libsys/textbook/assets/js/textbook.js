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
  self.pageContent = ko.observable();
  self.next_page = 0;
  self.previous_page = 0;
 
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
	 if(response.next) {
	   self.next_page = response.next;
	 } else {
           self.next_page = page_id;
         }
	 if(response.previous) {
	   self.previous_page = response.previous;
	 } else {
           self.previous_page = page_id;
	 }
     }
   });    

  }

  self.nextPage = function() {
    self.loadPage(self.next_page);
  };

  self.previousPage = function() {
    self.loadPage(self.previous_page);
  };
}
