<?xml version="1.0" ?>
<xsl:stylesheet
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:c="http://cnx.rice.edu/cnxml"
  xmlns="http://cnx.rice.edu/cnxml"
  version="1.0">


<!-- Identity tranform -->
<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>



<!-- Inject a label when a note contains a certain class -->
<xsl:template match="c:note[not(c:label)][@class]">
  <xsl:variable name="class" select="concat(' ', @class, ' ')"/>
  <xsl:copy>
    <xsl:apply-templates select="@*"/>

    <xsl:choose>
      <xsl:when test="contains($class, ' bringhome ')"><label>Bring it Home</label></xsl:when>
      <xsl:when test="contains($class, ' clearup ')"><label>Clear it Up</label></xsl:when>
      <xsl:when test="contains($class, ' workout ')"><label>Work it Out</label></xsl:when>
      <xsl:when test="contains($class, ' linkup ')"><label>Link it Up</label></xsl:when>
      <xsl:when test="contains($class, ' chapter-objectives ')"><label>Objectives</label></xsl:when>
      <xsl:otherwise/>
    </xsl:choose>

    <xsl:apply-templates select="node()"/>
  </xsl:copy>
</xsl:template>

</xsl:stylesheet>
