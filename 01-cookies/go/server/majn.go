package main

import (
	"log"
	"net/http"
	"time"
)

var PORT = ":8000"

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/set", authenticate)
	mux.HandleFunc("/authenticate", authenticate)

	log.Printf("Listening on port %v", PORT)
	log.Fatal(http.ListenAndServe(PORT, mux))
}

// setCredentials http handler that create the cookies
func setCredentials(w http.ResponseWriter, r *http.Request) {
	// create an instance of http.Cookie with the values received from the query params of the request
	cookie := http.Cookie{
		Name:    r.URL.Query().Get("id"),
		Value:   r.URL.Query().Get("name"),
		Expires: time.Now().Add(time.Minute * 15),
	}

	http.SetCookie(w, &cookie)

	w.Write([]byte("registered"))
}

// authenticate http handler that validate the cookies from the request
func authenticate(w http.ResponseWriter, r *http.Request) {
	cookie, err := r.Cookie(r.URL.Query().Get("id"))

	// check that cookies exist, if they do not exist, a forbidden status code is sent in response
	if err != nil {
		switch err {
		case http.ErrNoCookie:
			http.Error(w, "missing cookie", http.StatusForbidden)
		default:
			http.Error(w, "server error", http.StatusInternalServerError)
		}
		return
	}

	w.Write([]byte(cookie.Value))
}
