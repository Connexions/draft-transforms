<xsl:stylesheet

  xmlns:c="http://cnx.rice.edu/cnxml"
  xmlns:md="http://cnx.rice.edu/mdml"
  xmlns:col="http://cnx.rice.edu/collxml"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  version="1.0">


<!-- Identity transform for most things -->
<xsl:template match="@*|node()">
  <xsl:copy>
    <xsl:apply-templates select="@*|node()"/>
  </xsl:copy>
</xsl:template>


<xsl:template match="c:link[@document][not(@target-id)][not(text())]">
  <xsl:variable name="text">
    <xsl:choose>

<xsl:when test="@document = 'm48590'">Welcome to Economics!</xsl:when>
<xsl:when test="@document = 'm48602'">Choice in a World of Scarcity</xsl:when>
<xsl:when test="@document = 'm48628'">Demand and Supply</xsl:when>
<xsl:when test="@document = 'm48636'">Labor and Financial Markets</xsl:when>
<xsl:when test="@document = 'm48611'">Elasticity</xsl:when>
<xsl:when test="@document = 'm48640'">Consumer Choices</xsl:when>
<xsl:when test="@document = 'm48620'">Cost and Industry Structure</xsl:when>
<xsl:when test="@document = 'm48645'">Perfect Competition</xsl:when>
<xsl:when test="@document = 'm48650'">Monopoly</xsl:when>
<xsl:when test="@document = 'm48658'">Monopolistic Competition and Oligopoly</xsl:when>
<xsl:when test="@document = 'm48661'">Monopoly and Antitrust Policy</xsl:when>
<xsl:when test="@document = 'm48668'">Environmental Protection and Negative Externalities</xsl:when>
<xsl:when test="@document = 'm48675'">Positive Externalitites and Public Goods</xsl:when>
<xsl:when test="@document = 'm48681'">Poverty and Economic Inequality</xsl:when>
<xsl:when test="@document = 'm48689'">Issues in Labor Markets: Unions, Discrimination, Immigration</xsl:when>
<xsl:when test="@document = 'm48694'">Information, Risk, and Insurance</xsl:when>
<xsl:when test="@document = 'm48697'">Financial Markets</xsl:when>
<xsl:when test="@document = 'm48701'">Public Choice</xsl:when>
<xsl:when test="@document = 'm48705'">The Macroeconomic Perspective</xsl:when>
<xsl:when test="@document = 'm48713'">Economic Growth</xsl:when>
<xsl:when test="@document = 'm48719'">Unemployment</xsl:when>
<xsl:when test="@document = 'm48724'">Inflation</xsl:when>
<xsl:when test="@document = 'm48731'">The International Trade and Capital Flows</xsl:when>
<xsl:when test="@document = 'm48739'">The Aggregate Supply-Aggregate Demand Model</xsl:when>
<xsl:when test="@document = 'm48749'">The Keynesian Perspective</xsl:when>
<xsl:when test="@document = 'm48756'">The Neoclassical Perspective</xsl:when>
<xsl:when test="@document = 'm48761'">Money and Banking</xsl:when>
<xsl:when test="@document = 'm48768'">Monetary Policy and Bank Regulation</xsl:when>
<xsl:when test="@document = 'm48776'">Exchange Rates and International Capital Flows</xsl:when>
<xsl:when test="@document = 'm48791'">Government Budgets and Fiscal Policy</xsl:when>
<xsl:when test="@document = 'm48800'">The Macroeconomic Impacts of Government Borrowing</xsl:when>
<xsl:when test="@document = 'm48811'">Macroeconomic Policy Around the World</xsl:when>
<xsl:when test="@document = 'm48818'">International Trade</xsl:when>
<xsl:when test="@document = 'm48824'">Globalization and Protectionism</xsl:when>

      <xsl:otherwise>__NOTHING__</xsl:otherwise>
    </xsl:choose>
  </xsl:variable>

  <xsl:copy>
    <xsl:apply-templates select="@*"/>
    <xsl:choose>
      <xsl:when test="$text != '__NOTHING__'">
        <xsl:message>Adding Chapter title: <xsl:value-of select="$text"/></xsl:message>
        <xsl:attribute name="class">
          <xsl:value-of select="@class"/>
          <xsl:if test="@class"><xsl:text> </xsl:text></xsl:if>
          <xsl:text>target-chapter</xsl:text>
        </xsl:attribute>
        <xsl:value-of select="$text"/>
      </xsl:when>
      <xsl:otherwise>
        <xsl:apply-templates select="node()"/>
      </xsl:otherwise>
    </xsl:choose>
  </xsl:copy>

</xsl:template>

</xsl:stylesheet>
