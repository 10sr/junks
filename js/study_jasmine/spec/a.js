describe('Hello test', function(){
  it('should fail', function(){
    expect(1).toEqual(2);
  });

  it('should fail for add function', function(){
    expect(src.add(1,2)).toEqual(2);
  });
});
