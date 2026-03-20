package main//Главный пакет. Main - точка входа в программу

import("encoding/json" "fmt" "log" "net/http" "strings")
//Создаем модель пользователя
type User struct{
	ID int `json: "id"`
	Username string `json: "username"`
	Email string `json: "email"`
}
//users - База данных в памяти
var users=[]User{
	{ID:1,Username:"Alise", Email:"alice@example.com"},
	{ID:2,Username:"Jenek", Email:"jenek@example.com"},
}
//main - точка входа
func main(){
	//Обработчик для GET
	http.HandleFunc("/users", getUsers)
	//Обработчик для post //Создает нового пользователя
	http.HandleFunc("/users/create", createUser)
	//Запускаем сервер на порту 8080
	log.Println("Сервер запущен на http//localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
func getUsers(w http.ResponseWriter, r *http.Request){
	w.Header().Set("Content-Type", "aplication/json")
	json.newEncoder(w).Encode(users)
}
func createuser(w http.ResponseWriter, r*http.Request){
	if r.method=http.MethodPost{
		http.Error(w,"Метод не поддерживается ", http.StatusMethodNotAllowed)
		return
	}
	//Переменная куда будем декодировать  json
	var newuser User
	err:=json.newDecoder(r.body).Decode(&newuser)
	if err!=nil{
		http.Error(w."Неверный json", http.StatusBadRequest)
		return
	}
	//Валидация. Проверка что поля не пустые
	if strings.TrimSpace(newuser.Username)==""||strings.TrimSpace(newuser.Email)==""{
		http.Error(w, "Username и email обязательны", http.StatusBadRequest)
		return
	}
	//Генерируем новый id
	newID:=user[len(users)-1].ID+1
	newUser.ID=newID
	users=append(users, newUser)
	w.Header().Set("Content-type", "application/json")
	w.WrtieHeader(http.StatusCreated)
	json.newEncoder(w).Encode(newuser)
}