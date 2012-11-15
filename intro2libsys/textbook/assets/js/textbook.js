function TextbookPageViewModel() {
  // Data
  var self = this;
  self.currentPage = ko.observable();
  self.pageContent = ko.observable();

  // Behaviours
  self.nextPage = function() {
    alert("In nextPage " + location.hash);
  };

  self.previousPage = function() {
    alert("In previousPage " + location.hash);
  };


}
