package main
	"context"
	"encoding/json"
	"errors"
	"github.com/go-kit/kit/endpoint"
	httptransport "github.com/go-kit/kit/transport/http"
	"net/http"
	"strings"
// 首先定义一个服务的接口， 将我们的功能暴露出来
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
// ================================================================
 * 通过上下文定义的接口、报文， 我们实现 对应的 RPC 对象： endPoint
func makeUppercaseEndpoint(svc StringService) endpoint.Endpoint{
	return func(_ context.Context, request interface{}) (interface{}, error) {
		req := request.(uppercaseRequest)
		v, err := svc.Uppercase(req.S)
		if err != nil {
			return uppercaseResponse{v, err.Error()}, nil
		return uppercaseResponse{v, ""}, nil
func makeCountEndpoint(svc StringService) endpoint.Endpoint {
	return func(_ context.Context, request interface{}) (response interface{}, err error) {
		req := request.(countRequest)
		v := svc.Count(req.S)
		return countResponse{v}, nil
// 针对请求报文和返回报文，我们定义了其格式
type uppercaseRequest struct {
	S string `json:"s"`
type uppercaseResponse struct {
	V string `json:"v"`
	Err string `json:"err, omitempty"`
type countRequest struct {
	S string `json:"s"`
type countResponse struct {
	V int `json:"v"`
// 服务启动的主入口
func main() {
	svc := stringService{}
	uppercaseHandler := httptransport.NewServer(
		makeUppercaseEndpoint(svc),
		decodeUppercaseRequest,
		encodeResponse,
	countHandler := httptransport.NewServer(
		makeCountEndpoint(svc),
		decodeCountRequest,
		encodeResponse,
	http.Handle("/uppercase", uppercaseHandler)
	http.Handle("/count", countHandler)
	log.Fatal(http.ListenAndServe(":8080", nil))
func decodeUppercaseRequest(_ context.Context, r *http.Request) (interface{}, error) {
	var request uppercaseRequest
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		return nil, err
	return request, nil
func decodeCountRequest(_ context.Context, r *http.Request) (interface{}, error) {
	var request countRequest
	if err := json.NewDecoder(r.Body).Decode(&request); err != nil {
		return nil, err
	return request, nil
func encodeResponse(_ context.Context, w http.ResponseWriter, response interface{}) error {
	return json.NewEncoder(w).Encode(response)
