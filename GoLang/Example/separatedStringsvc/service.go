package main
	"errors"
	"strings"
type StringService interface{
	Uppercase(string) (string, error)
	Count(string) int
// 针对上面接口，我们提供了实现类
type stringService struct {}
func (stringService) Uppercase(s string) (string, error) {
	if s == "" {
		return "", ErrEmpty
	return strings.ToUpper(s), nil
func (stringService) Count(s string) int {
	return len(s)
var ErrEmpty = errors.New("Empty string")
