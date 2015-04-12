$(onLoad)

//------------------------------------------------------------------------------
function onLoad() {
  uiLoad("loaded")
  setInterval( 500, refreshData)
  setInterval(1000, generateNewData)
}

//------------------------------------------------------------------------------
function uilog(string) {
  $(".console").append(string + "\n")
}

//------------------------------------------------------------------------------
function refreshData() {
  $.ajax("/api/data", {
    dataType: "json",
    success:  refreshSuccess,
    error:    refreshError
  })
}

//------------------------------------------------------------------------------
function refreshSuccess(data, status, jqXHR) {
  uiLog(JSON.stringify(data))
}

//------------------------------------------------------------------------------
function refreshError(jqXHR, status, error) {
  console.log("error refreshing: ", error)
}

//------------------------------------------------------------------------------
function generateNewData() {
}
