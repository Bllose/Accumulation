package greetings
	"errors"
	"math/rand"
func Hello(name string) (string, error) {
	if name == "" {
		return "", errors.New("EMPTY NAME")
	message := fmt.Sprintf(randomFormat(), name)
	return message, nil
func Hellos(names []string) (map[string]string, error) {
	// In Go, you initialize a map with the following syntax: make(map[key-type]value-type)
	messages := make(map[string]string)
	// In this for loop, range returns two values: the index of the current item in the loop
	// and a copy of the item's value. You don't need the index, so you use the Go blank iden-
	// -tifier(an underscore) to ignore it.
	for _, name := range names {
		message, err := Hello(name)
		if err != nil {
			return nil, err
		messages[name] = message
	return messages, nil
func init() {
	rand.Seed(time.Now().UnixNano())
func randomFormat() string {
	// a slice of message formats. A slice is like an array, except that its size changes dynamically
	// as you add and remove items.
	formats := []string{
		"Hi, %v. Welcome!",
		"Great to see you, %v!",
		"Hail, %v! Well met!",
	return formats[rand.Intn(len(formats))]
